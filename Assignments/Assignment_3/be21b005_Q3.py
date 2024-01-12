# We need to find the minimum number of operations (involving adding or subtracting 1) to make the product of list equal to 1.
# This is possible only if the list is composed of either only 1's.
# Or also if list is composed of 1's and -1's, but the number of -1's is even.
# So, basically, we first need our list to have only 1's and -1's
# Also, if we have 0's in our list, then they can be converted to 1 or -1 in equal number of steps.
# Converting 0 into 1 or -1 will require 1 step.
def minop(n, a):
    # count will be counting the number of operations
    count = 0
    # count_zero will count the number of zeros in the list
    count_zero = 0
    # count_neg_one will count the number of -1's in the list
    count_neg_one = 0
    for i in range(n):
        if(a[i]>0):
            # If the value of an element is greater than zero, then naturally, we have to reduce it to 1,
            # And this task will require a[i] - 1 steps, (Ex. elements 6 will require 5(6-1) operations of removal to reach 1)
            count += a[i]-1
        elif(a[i]<0):
            # If the value of an element is lesser than zero, then naturally, we have to increase it to -1,
            # And this task will require -(a[i] - 1) steps, (Ex. elements -6 will require 5(-(-6+1)) operations of addition to reach -1)
            count += -(a[i]-(-1))
            count_neg_one += 1
        else:
            count_zero += 1
    # If the number of zeros is greater than 0, then we don't have to worry about the number of of -1's being even or not.
    # Because we can be sure that by adding count_zero steps, we are getting the right count to reach list product 1.
    # If we have odd number os -1's, then we can convert one 0 to -1 and rest to +1
    # If we have even number of -1's then we can convert all 0's to +1
    if(count_zero > 0):
        count += count_zero
    # However, if the number of 0's is zero and number of -1's is not even,
    # Then we need to perform a 2 step operation to either convert a -1 to +1 or +1 to -1
    elif(count_neg_one%2 !=0 and count_zero == 0):
        count += 2
    # This will give us the effective count we desire.
    return count
# Since we are iterating through the list only once, the time complexity of above algorithms is O(N).

print(minop(3, [1,2,1]))
print(minop(5, [1,2,3,4,6]))
print(minop(4, [-5,-1,8,7]))