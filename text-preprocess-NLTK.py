# Analyzing Text with NLTK.

#==========================
# Author: Marjan Khamesian
# Date: July 2020
#==========================

import nltk
import pandas as pd
import string

book = open("Wonderland.txt", "r")
#print(book.read())

text = book.read()
my_lst = text.splitlines()
#print(my_lst)

# Create a DataFrame
df = pd.DataFrame({'Sentence':my_lst})
#print(df.head())

# Lowercase
df['Sentence'] = df['Sentence'].str.lower()
#print(df)

print(type(df['Sentence']))
print(type(df['Sentence'][1]))

# Removing punctuations
def remove_punctuations(df):
    for punctuation in string.punctuation:
        df = df.replace(punctuation, '')
    return df

# Applying the function to the DataFrame
df['Sentence'] = df['Sentence'].apply(remove_punctuations)
print(df['Sentence'].head())

# Removing Numbers
df['Sentence'] = df['Sentence'].str.replace('\d+','')
print(df['Sentence'].head())

# ==============================
# Removing stop words with NLTK 
# ==============================
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print('Stop Words:')
print(stop_words)

df['Sentence'] = df['Sentence'].apply(
    lambda x: " ".join(x for x in x.split() if x not in stop_words))

print(df['Sentence'].head())

# ===============
# Tokenizing text
# ===============
# to split a sentence into words
from nltk.tokenize import word_tokenize

tokens = [word_tokenize(i) for i in my_lst]

for i in tokens:
    print(i)

# ========
# Stemming
# ===============
# Snoball Stemmer
from nltk.stem.snowball import SnowballStemmer

SnowballStemmer = SnowballStemmer('english')
stem_df = df['Sentence'][:6].apply(
    lambda x: " ".join([SnowballStemmer.stem(word) for word in x.split()]))

print('Stemmimg')
print(stem_df)
