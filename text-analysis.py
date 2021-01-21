# Program for Analysing a Book.
#
# This program is based on an exercise from Think Python book.
# The idea is to see how many words are there in a text.
# It reads a text, breaks each line into words,
# strips whitespace and punctuation from the words,
# and converts them to lowercase.
#
# ===============================
# Author: Marjan Khamesian
# Date: March 2020
# ===============================
import string

# loops through the lines,                                                                
# passing them one at a time to process_line:                                                         

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

# replace hyphens with spaces
def process_line(line, hist):
    line = line.replace('-', ' ')
    
    # break the line into a list of strings
    for word in line.split():

        # remove punctuation
        word = word.strip(string.punctuation + string.whitespace) 

        # convert to lower case
        word = word.lower()
        
        hist[word] = hist.get(word, 0) + 1

hist = process_file('ironmask.txt')

# To count the total number of words in the file:
def total_words(h):
    return sum(h.values())

# The number of different words:
def different_words(h):
    return len(h)

# Print the results
print('The text contains', total_words(hist), 'words')
print("\n================================\n")
print('Number of different words:', different_words(hist))





