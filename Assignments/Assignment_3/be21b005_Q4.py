import math
# Below is a Stack class
# I will be using stacks in two ways
# In InfixToPostfix, to store the order of operators.
# In EvaluatePostfix, to store the operands in right order.
class Stack:
    # Initially an empty list on creating of a stack object.
    def __init__(self):
        self.arr = []
      
    # Checking if the given list is empty.
    def is_empty(self):
        if(len(self.arr) == 0):
            return True
        return False
    
    # Appending a value to the list on receiving a push operation.
    def push(self, value):
        self.arr.append(value)
    
    # Removing the topmost value from the list and returning it to the call point.
    def pop(self):
        return self.arr.pop()

    # Returning the topmost value from the list, without removing it from the list.
    def peak(self):
        return self.arr[-1]
    
    # Printing the list whenever needed(mainly for debugging times).
    def __str__(self):
        return str(self.arr)

def InfixToPostfix(infix):
    # Initializing a postfix list to []
    postfix = []
    s = Stack()
    # hierarchy is a dictionary to decide the precedence of operators, [^] > [*,/] > [+,-]
    hierarchy = {"+":1, "-":1, "*":2, "/":2, "^":3}
    # The role of check is to account for integers with place value greater than one unit.
    check = False
    for i in range(len(infix)):
        # If the element is not an operator, nor an ( or ) parenthesis, then directly append to postfix list.
        if(infix[i] not in hierarchy and infix[i] != "(" and infix[i] != ")"):
            if(check == True):
                # If check s true, then the elements is added to the previous number in the previous iteration.
                # Ex. If 1 was the previous iteration, and current iteration is 0, then I update the value to 10.
                # This is because, if we have two numeric values adjacent, then they represent a complete number.
                postfix[-1] = str(postfix[-1]+infix[i])
            else:
                postfix.append(infix[i])
                check = True
                
        # On encountering an open parenthesis, push it to the stack.
        elif(infix[i] == "("):
            s.push(infix[i])
            # check is false because this is not a number.
            check = False
            
        # On encountering a closed parenthesis,
        elif(infix[i] == ")"):
            # We need to keep appending the operators to postfix, till either the stack empties or you encounter a "(".
            # Because, encounteringa "(" would imply the role of ")" was limited till there only.
            while(not s.is_empty() and s.peak() != "("):
                postfix.append(s.pop())
            # This situation arises, when you encounter a "(".
            # Then we just pop the element "(", without storing it, because its purpose has been served.
            if(not s.is_empty()):
                s.pop()
            # check is false, because this is not a number.
            check = False
            
        else:
            # This is when the current element is an operator.
            # If stack is empty or the topmost value is "(", then just push the operator.
            # But if topmost value of stack is not "(", then check for hierarchy of the current and topmost operator.
            # If current operator is less than or equal to the topmost operator, in terms of hierarchy,
            # append the operators in the stack to the postfix, till you encounter a "(" or a higher hierarchy or empty stack.
            while(not s.is_empty() and s.peak() != "("):
                if(hierarchy[infix[i]] <= hierarchy[s.peak()]):
                    postfix.append(s.pop())
                else:
                    break
            
            # Once you have removed the operators based on above conditions, push the current operator to stack.
            s.push(infix[i])
            # check is false, because this is not a number.
            check = False
    
    # Now, when we have reached the end of infix statement, keep appending the topmost values of stack to the postfix
    # till you empty the stack completely.
    while(not s.is_empty()):
        postfix.append(s.pop())
        
    # Now, we have the postfix list ready.
    return postfix

def EvaluatePostfix(postfix):
    # The postfix list has only numbers and operators.
    # Stack is created to store the numbers.
    s = Stack()
    # Hierarchy here in only for the sake of considering the operators, the very concept is not needed here.
    hierarchy = {"+":1, "-":1, "*":2, "/":2, "^":3}
    for i in range(len(postfix)):
        # If current element is not an operator, then append it to the stack.
        if(postfix[i] not in hierarchy):
            s.push(postfix[i])
        
        # else implies the current element is an operator.
        else:
            # Remove the top two elements of the stack into element1 and element2, where element1 will be the lower in stack.
            element2 = float(s.pop())
            element1 = float(s.pop())
            # If the operator is "+", then add element1 and element2
            if(postfix[i] == "+"):
                val = element1 + element2
            # If the operator is "-", then subtract element2 from element1
            elif(postfix[i] == "-"):
                val = element1 - element2
            # If the operator is "*", then multiply element1 and element2
            elif(postfix[i] == "*"):
                val = element1 * element2
            # If the operator is "/", then divide element2 by element1
            elif(postfix[i] == "/"):
                val = element1 / element2
            # else the operator is "^", then take element1 raised to the power element2
            else:
                val = math.pow(element1, element2)
            # push this new value from operation into the stack.
            s.push(str(val))
    # MY final stack will have only 1 value and that is the result of the postfix operation.
    return s.pop()

infix = "3^4/(5*6)+10"
postfix = InfixToPostfix(infix)
print("Postfix Expression:", postfix)
result = EvaluatePostfix(postfix)
print("Result:", result)