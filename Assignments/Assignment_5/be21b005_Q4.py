import re
import matplotlib.pyplot as plt 

# File location is stored in words_file
words_file = "C:\\Users\\Dell\\Desktop\\Courses\\Sem_V\\DSA\\Graded_Assignments\\Assignment_5\\words.txt"
# Since the file is too big, no need to store the string lines of the file anywhere   

"""
Given words.txt as a file: with all words in lower case itself
Find the number of words in words.txt that satisfy each criteria
"""
count_a = 0
count_b = 0
count_c = 0
count_d = 0

"""
(a) Word starts with a vowel and ends with a consonant
(b) Words that contain at least 3 a's
(c) Word has repeated alphabets consecutively
    (Ex: (i) aardvark, 'a' repeats twice at start, (ii) abasia should not match here)
(d) Word starts and ends with the same vowel (Ex: abasia)

"""
# Define a patterns satisfying the above conditions
# Pattern for "word starts with a vowel and ends with a consonant"
# ^[aeiou] checks for whether word starts with a vowel
# [^aeiou]$ checks for whether word ends with a vowel 
pattern_a = "^[aeiou].*[^aeiou]$"
# Pattern for "words that contain at least 3 a’s"
# The three a's imply that three a are expected in the word
# The .* could be anything. It could even be a ( in case of a's more than 3)
pattern_b = ".*[a].*[a].*[a].*"
# Pattern for "word has repeated alphabets consecutively"
# Start could be anything. We should have 1 elements(a-z), immediately followed by the same element.
# That is why we group the first [a-z] and check its consecutive location with \\1 for same letter
pattern_c = ".*([a-z])\\1.*"
# Pattern for "word starts and ends with the same vowel"
# ^([aeiou]) checks for whether word starts with a vowel
# The above has been group and given \\1$, to ensure the word ends with the same vowel, it started with
pattern_d = "^([aeiou]).*\\1$"

# Open the file for reading
with open(words_file, 'r') as f:
    for line in f:
        # Check for pattern matching with every word and increment corresponding count
        line = line[:-1]
        matches1 = re.search(pattern_a, line)
        if(matches1):
            count_a += 1
        matches2 = re.search(pattern_b, line)
        if(matches2):
            count_b += 1
        matches3 = re.search(pattern_c, line)
        if(matches3):
            count_c += 1
        matches4 = re.search(pattern_d, line)
        if(matches4):
            count_d += 1

# Print the respective counts
print(count_a)
print(count_b)
print(count_c)
print(count_d)