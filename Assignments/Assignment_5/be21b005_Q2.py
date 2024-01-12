import random
import matplotlib.pyplot as plt
# define a function birthday_problem as directed in the question
# n is the group size we are considering
def birthday_problem(n):
    # num is the assumed number of iterations
    num = 10000
    # number of people who share birthday is stored in share_birthday
    share_birthday = 0
    # probability stores the cumulative ratio of number of experiments having shared birthdays and total number of experiments
    probability = []
    for i in range(num):
        # dates will store random birthdays of group size number of people
        dates = []
        for j in range(n):
            # a person can have his birthday on a random day in a year of 365 days.
            # we assume that a year has 365 days. We are ignoring the leap years
            dates.append(random.randint(0,364))
        # set will store the non repeated elements in the dates list
        dates_set = set(dates)
        # If length of dates_set is equal to length of dates, it means no repeated occurence, i.e., no shared birthday
        if(len(dates) != len(dates_set)):
            # share_birthday only if the above condition holds
            share_birthday += 1
        # Finding the probability from the experiments so far
        probability.append(share_birthday/(i+1))
    # return probability
    return probability

# Choose the number of people among which you want to find the probability of sharing birthdays
num_people = 30
# Call the function
prob = birthday_problem(num_people)
print(prob[-1])
# Plot the probability list
plt.plot(prob, color="blue")
plt.show()