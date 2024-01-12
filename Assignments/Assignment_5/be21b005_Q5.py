import re

# HH FORMAT
# The pattern allows all 0-9 as second digit if first digit is 0 or 1.
# If first digit is 2, only 0,1,2,3 are allowed as second digit
# No other 1st digit is allowed.

# MM FORMAT
# For 1st digit between 0-5 all 0-9 digits are allowed for second digit
pattern = "(^[01][0123456789]|^[2][0123]):[012345][0123456789]$"

# Sample test case
txt = "23:59"
# Check for match. If matches print "Matched" else print "Not matched"
match = re.search(pattern,txt)
if(match):
    print("Matched")
else:
    print("Not matched")