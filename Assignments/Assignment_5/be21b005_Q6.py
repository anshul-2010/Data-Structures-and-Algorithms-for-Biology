import re

# File location is stored in data_file
data_file = "C:\\Users\\Dell\\Desktop\\Courses\\Sem_V\\DSA\\Graded_Assignments\\Assignment_5\\Data.txt"

# all_cust will store the entire list of customers after removing the indentations and numbering present in the text
all_cust = []
# Reading through each line of data_file, to ignore the numberings and indentation
# and store only the customer specific details, for all customers, in the all_cust list
with open(data_file, 'r') as f:
    # customer stores one customers details in a dictionary
    customers = {}
    for line in f:
        # The last position will have \n, so remving that from the line
        line = line[:-1]
        # match the respective criteria and add it to the dictionary under the same keyword
        # We add the details from "two" indices after ":" all the way until the "end" of the line for each case
        if(re.match(".*Name:.*", line)):
            customers["Name"] = line[line.index(':')+2:len(line)]
        elif(re.match(".*Age:.*", line)):
            customers["Age"] = line[line.index(':')+2:len(line)]
        elif(re.match(".*Email:.*", line)):
            customers["Email"] = line[line.index(':')+2:len(line)]
        elif(re.match(".*Address:.*", line)):
            customers["Address"] = line[line.index(':')+2:len(line)]
        elif(re.match(".*Phone:.*", line)):
            customers["Phone"] = line[line.index(':')+2:len(line)]
        else:
            # When we encounter none of the required details, append it to all_cust if customers is not empty
            # also make the customers empty for subsequent rounds
            if(customers!={}):
                all_cust.append(customers)
                customers = {}
    # We might be left with one customer towards the end, so if we find so, append it
    if(customers != {}):
        all_cust.append(customers)  

# Now, we need to check for address with either no vowels or atleast 4 vowels, using address_pattern regex expression
# (^.*([aeiouAEIOU].*) this grouped element checks for presence of a vowel anywhere in that string. Using {4,} with
# the above ensures that to check for vowels 4 or more number of times in the string.
# Alternative case is [^aeiouAEIOU]*, where start through end, no vowel is present
# Since address has upper and lower cases, we check for the both extremes
address_pattern = "((^.*([aeiouAEIOU].*){4,}$)|^[^aeiouAEIOU]*$)"
# We store the new set of people who undergo address level shortlist in better_cust
better_cust = []
for i in range(len(all_cust)):
    match = re.search(address_pattern, all_cust[i]["Address"])
    if match:
        better_cust.append(all_cust[i])

# Now, we need to shortlist the people who don't have google account.
# I am assuming "gmail.com" and "google.com" as the email extensions that indicate google account
shortlist = []
# Checking @ followed by gmail or google will check for google accounts
email_pattern = ".*@(gmail|google).*"
# The customer is shortlisted only if his/her email id doesn't have the email_pattern in it
for i in range(len(better_cust)):
    if not (re.match(email_pattern,better_cust[i]["Email"])):
        shortlist.append(better_cust[i])

# print the details of the shortlisted people, especially the address, so as to send the money across
for i in range(len(shortlist)):
    print(shortlist[i])
    print("ADDRESS -------", shortlist[i]["Address"])