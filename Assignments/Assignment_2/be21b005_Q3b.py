# A FASTA file format has an ID and also the sequence for a certain number of genes.
# The ID starts with the expression ">"
import re
# Defining "f" as an identifier for the dna.fasta file
f = open('C:\\Users\\Dell\\Downloads\\dna.fasta','r')
# The option "r" means read only
# Reading all the lines and storing it in a list format for easy accessibility.
lines = f.readlines()

# Below are the regex expressions to look for the ID and gene sequences
# id_find compiles and matches the lines that begin with the expression ">"
id_find=re.compile('>(\S+)')
# sequence_find compiles and matches the lines with the gene sequences
sequence_find = re.compile('^(\S+)$')

# 'gene' dictionary will store the ID as key and the sequence as value.
gene={}

# Iterating through each line read from the file.
for line in lines:
    # Checking if the line has ID
    outh = id_find.search(line)
    if outh:
        id=outh.group(1)
    else:
        # If not ID, check for the sequence
        outl=sequence_find.search(line)
        # If ID present, store the corresponding sequence.
        if(id in gene.keys()):
            gene[id] += outl.group(1)
        else:
            gene[id]  =outl.group(1)

# The sequence is extracted from the gene dictionary                        
sequence = gene['test_for_primer_question']
# printing the sequence
print(sequence)

# The function 'invert' is to reverse the DNA sequence received as input
def invert(six_bp):
    reverse = ""
    for i in range(len(six_bp)-1,-1,-1):
        reverse += six_bp[i]
    return reverse

# The function 'palindrome' is to check if the given DNA sequence is a
# palindromic DNA sequence or not.
def palindrome_2():
    comp = {"A":"T","T":"A","G":"C","C":"G"}
    count = 0
    
    # Given in the question to consider base pair length could be anything.
    # I shall consider that the length of base pair is greater than or equal
    # to 2 because a single base pair cannot be considered a palindromic sequence.
    for base_pairs in range(2, len(sequence)):
        for i in range(len(sequence)-(base_pairs-1)):
            six_bp = sequence[i:i+base_pairs]
            reverse = invert(six_bp)
            complement = ""
            for i in range(len(six_bp)):
                complement += comp[six_bp[i]]
            if(reverse==complement):
                count += 1
    return count

print(palindrome_2())

# The above code takes every n consecutive characters, from the DNA sequence and 
# checks if it obeys the palindromic sequence condition or not.
# Here, n ranges from '2' to 'len(sequence)'
# If satisfied, count is incremented.