import random
import math
import matplotlib.pyplot as plt

# Total number of iterations in random number analysis
n = 10000
# Number of points that lie inside the ellipse
inside_points = 0
# a represents a quantity in the major axis of the ellipse
a = 2
# b represents a quantity in the minor axis of the ellipse
b = 1
# Making a list of true values to compare against my values
true_value = [math.pi*a*b]*n
# area will store the area obtained at each iteration by the random number method
area = []
# stores the error at each iteration
error = []
for i in range(n):
    # sampling random x and y coordinatees within the range of rectangle bounding the ellipse
    x = a*random.random()
    y = b*random.random()
    # Defining c that will check whether the point lies inside or outside the ellipse
    c = (x**2)/(a**2) + (y**2)/(b**2)
    if(c<1):
        # If point inside, increment inside_points
        inside_points += 1
    # Area of ellipse / Area of rectangle = inside_points / total iterations
    # Area of rectangle is (2a)*(2b) = 4ab, hence to find area of ellipse, the following is appended
    area.append(4*a*b*(inside_points/(i+1)))
    # error is absolute subtraction of true_val at that index and area at that index
    error.append(abs(true_value[i] - area[-1]))
    
# Print error values at 100, 1000, 10000 th positions to see how it changes.
print(error[99])
print(error[999])
print(error[9999])
# Plot the area as well as error graphs, along with their true values
plt.figure(figsize=(16,6))
plt.plot(true_value, linestyle="dashed", color="blue")
plt.plot(area, color="red")
plt.show()
plt.plot([0]*n, linestyle="dashed", color="blue")
plt.plot(error, color="red")
plt.show()


"""
When the number of random points increases, more and more area starts filling up with points(the randomly chosen ones)
and ideally we start getting a better approximation of the area. It is just more probable that the approximation value
gets better and better. However, it is not absolutely guaranteed, whatsoever. That is why, you can observe the graph
going up and down.
"""