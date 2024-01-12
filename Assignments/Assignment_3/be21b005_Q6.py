# agent_veda takes in the given input and returns an integer that corresponds to the count of possible prism locations.
# The logic I am using is,
# I begin from the rightmost column, from the bottommost element.
# As I move up a column, if I encounter a clear pathway, I will increment the count and move up.
# If I encounter a barrier, then I will no longer increment the count for that particular column and move on to the next column.
def agent_vega(chamber):
    # vision will store 0 or 1 depending on whether that particular row is accessible for person anymore.
    # vision will store all the laser barriers in a column as 0.
    vision = []
    for i in range(len(chamber)):
        # Initializing the vision to 0 or 1 depending on the rightmost column.
        if chamber[i][-1] == "#":
            vision.append(0)
        else:
            vision.append(1)
    # count will store the number of possible prism locations.
    count = 0
    for i in range(len(chamber)-1, -1, -1):
        # possible will be used to determine, till when while iterating in a column will count have to increase.
        # Till you encounter a # in the column, there is a possibility of a path to be found.
        # If # is found beyond that any path starting from the that column is not possible.
        possible = True
        for j in range(len(vision)-1, -1, -1):
            if(possible):
                # If . is found and its corresponding location in vision is 1(open), then count is incremented.
                if(chamber[j][i] == "."):
                    if(vision[j] == 1):
                        count += 1
                # else implies # is encountered, so we make its corresponding vision elements 0 because that row is no longer accessible from the left.
                else:
                    vision[j] = 0
                    # possible is False now, because I can no longer expect the above elements to be a correct path.
                    possible = False
            # If not possible, just find the #'s above and update its corresponding vision.
            else:
                if(chamber[j][i] == "#"):
                    vision[j] = 0
        
    return count

print(agent_vega([['#', '.', '.'], ['#','.', '.'], ['#','.', '.']]))
print(agent_vega([['#', '.', '#'], ['#','.', '#'], ['#','.', '#']]))