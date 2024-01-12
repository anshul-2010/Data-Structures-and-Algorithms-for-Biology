# For "n"th step: We can reach the "n"th step in three ways,
# 1. The number of ways to reach "n-1"th step + 1 step
# 2. The number of ways to reach "n-2"th step + 2 steps
# 3. The number of ways to reach "n-3"th step + 3 steps.
# So, the number of ways to reach "n"th step would be summation of previous three cases.
# Hence, we will be setting three base cases for n = 1,2,3 and recursively solve the question.
def numways(n):
    # First three cases are base cases for which we can directly return the correct values.
    if(n==1):
        return 1 # (1)
    elif(n==2):
        return 2 # (1+1, 2)
    elif(n==3):
        return 4 # (1+1+1, 1+2, 2+1, 3)
    else:
        a = 1 # Number of ways to reach the door, if only 1 step (1).
        b = 2 # Number of ways to reach the door, if only 2 step (1+1, 2).
        c = 4 # Number of ways to reach the door, if only 3 step (1+1+1, 1+2, 2+1, 3).
        while(n-3>0):
            a,b,c = b,c,a+b+c # Updating ways to reach the next step.
            n -= 1 
        return c # c will finally store the value corresponding to "n" number of stairs.
#  Since we are iterating through n only once, the time complexity of above algorithm is O(N).
print(numways(2))
print(numways(3))