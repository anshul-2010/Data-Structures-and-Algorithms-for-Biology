"""
f(x) = 1/x , integrating from 1/2 to 2

I (integral) = ln(x) ] from 1/2 to 2  = ln(2) - ln(0.5) = 2ln(2) = ln(4)

Area under the integral sign = Monte Carlo Integration Approximation
"""
import random
import matplotlib.pyplot as plt
import math
# n is the number of iterations
n = 10000
# value refers to the current value of function f(x) = 1/x
value = 0
# true value of e to compare against
true_val = [math.e]*n
# Calculates the e value based on analytically calculated solution of area in the previous cell
e_val = []

# The idea is to find the average y coordinate (1/x) value corresponding to x.
# The area is then calculated as that of rectangle with the y coordinate times the range of x
for i in range(n):
    # x will sample a random number between 1/2 and 2 from the uniform distribution
    x = random.uniform(1/2, 2)
    # Add the function to value
    value += 1/x
    # Find the average of value over the current number of iterations
    avg = value / (i+1)
    # area is the area of the rectangle so obtained with the average function value.
    area = avg*(2 - 1/2)
    # Find the corresponding value of e from the analytical solution by transfering across the equal sign
    e_val.append(2**(2/area))
print(e_val[-1])
# Plot the graph of true value as well as Monte Carlo method
plt.figure(figsize=(16,6))
plt.plot(true_val, linestyle="dashed", color="blue")
plt.plot(e_val, color="red")
plt.show()