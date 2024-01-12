# Below is an implementation of a Stack class
class Stack:
    # Initiating the list with the argument received at the time of creation of Stack object.
    def __init__(self, ar):
        self.arr = ar
        
    # Checking if the list is empty or not.
    def is_empty(self):
        if(len(self.arr) == 0):
            return True
        return False
    
    # Appends an element to the list.
    def push(self, value):
        self.arr.append(value)
    
    # Removes the topmost element from the list and returns it at the call point.
    def pop(self):
        return self.arr.pop()

    # Returns the topmost element from the list without removing it from the list.
    def peak(self):
        return self.arr[-1]
    
    # Printing the list(mainly for debugging).
    def __str__(self):
        return str(self.arr)

# Below is an implementation of a Queue class.
class Queue:
    # Initiating the list with the argument received at the time of creation of Queue object.
    def __init__(self, ar):
        self.arr = ar
        
    # Checks whether the queue is empty or not.
    def is_empty(self):
        if(len(self.arr) == 0):
            return True
        return False
    
    # Returns the current length of the queue.
    def length(self):
        return len(self.arr)
    
    # Appends an element to the end of the queue.
    def enqueue(self, value):
        self.arr.append(value)
    
    # Pops/Removes the first element of the queue from the list and returns the value to the call point.
    def dequeue(self):
        return self.arr.pop(0)

    # Returns the first element of the queue without removing it from the list.
    def peak(self):
        return self.arr[0]
    
    # Prints the queue(mainly for debugging).
    def __str__(self):
        return str(self.arr)

def numstd(students, sandwiches):
    # Below, create a Queue for the students, because the students behave the same way as the data structure "Queue".
    c = Queue(students)
    # Inverting the sandwiches list, because that it how it will suit the data structure stack defined above.
    sandwiches = sandwiches[::-1]
    # Create a Stack for the sandwiches, because it works in the same way as the data structure "Stack".
    s = Stack(sandwiches)
    # cant is used to count how many students can't eat the sandwiches.
    # It is used for the breaking condition to decide whether any student can eat the topmost sandwich or not.
    cant = 0
    
    while(not s.is_empty()):
        # If the topmost value of stack is equal to first value of queue,
        # remove the respective elements from stack and queue.
        if(s.peak() == c.peak()):
            s.pop()
            c.dequeue()
            cant = 0
        # else, just move the first element of queue to the last and increment value of cant
        else:
            c.enqueue(c.dequeue())
            cant += 1
        # If value of cant is equal to length of queue, that means that none of the students chose the topmost sandwich.
        # This implies that no student can take sandwich any more.
        if(cant == c.length()):
            break
            
    # The number of people who cant take sandwich are the number of people left uneaten.
    return cant

print(numstd([1,1,0,0], [0,1,0,1]))
print(numstd([1,1,1,0,0,1], [1,0,0,0,1,1]))