# We can use the inbuilt sorting algorithm too. But I have implemented MergeSort.
# Defining the merge algorithm to merge two lists at any level.
def merge(a,b): 
    # Defining an empty list c to store the merged result in sorted order.
    c = [None]*(len(a)+len(b))
    # Below three are the pointers for lists a, b, c initialized to zero.
    i = j = k = 0
    # Compare elements in lists a and b, and merge them to c.
    while(i<len(a) and j<len(b)):
        if(a[i]<b[j]):
            c[k] = a[i]
            i+=1
        else:
            c[k] = b[j]
            j+=1
        k+=1
    
    # Based on whether the remaining elements are in a or b, copy them to c directly.
    if(i<len(a)):
        c[k:] = a[i:]
    else:
        c[k:] = b[j:]
    
    # Return the merged and sorted list c, corresponding to a and b.
    return c

def MergeSort(a):
    n = len(a)
    if(len(a)==1):
        # Base case: If list has 1 element, list is already sorted.
        return a
    else:
        # Here, recursively split the list in half
        # Sort each half and then merge them together.
        return merge(MergeSort(a[:n//2]), MergeSort(a[n//2:]))
# The above sorting algorithm takes up a time complexity of O(nlogn)
    
# Major function to compute the maximum study group.
# We certainly know that students chosen will have contiguous skill values.
# i.e., if skills 3 and 5 are there in the group, then anyone with skill "4" will also be in the same group.
def maxstud(n,a):
    # Owing to above reason, we sort the list of skills.
    sort_a = MergeSort(a)
    # maximum is the largest possible sub-group that obeys the rule of grouping.
    maximum = 0
    # i and j are pointers to check the possible sub-groups.
    i = 0
    j = 0
    count = 0
    # So, the algorithm used is:
    # i to j basically forms the window, whose size we are trying to maximize 
    # j keeps increasing till the condition of "<=5" is satisfied.
    # Whenver that condition breaks, i increases, to bring the window back to obeying the conditions.
    # This continues till we reach the end of the list.
    # Also, at each instance, count is compared to maximum, to ensure we update the maximum value regularly.
    while(j < n):
        if((sort_a[j] - sort_a[i]) <= 5):
            count += 1
            j += 1
        else:
            count -= 1
            i += 1
        if(count>maximum):
            maximum = count
    return count
# The above algorithm takes up a time complexity of O(n).

# Hence the overall time complexity is O(nlogn + n), whick boils down to O(nlogn).
# Hence the time complexity is "O(NlogN)".

print(maxstud(5, [1,2,3,4,6]))
print(maxstud(4, [5,1,8,7]))