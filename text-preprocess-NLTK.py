# Analyzing Text with NLTK.

#==========================
# Author: Marjan Khamesian
# Date: July 2020
#==========================

import nltk
import pandas as pd
import string

book = open("Wonderland.txt", "r")
text = book.read()
my_lst = text.splitlines()
print(my_lst)

# ==================
# Create a DataFrame
df = pd.DataFrame({'Sentence':my_lst})
print(df.head())

# ===============
# Number of words                                                                                    
df['word_count'] = df['Sentence'].apply(lambda x: len(str(x).split(" ")))
num_words = df[['Sentence','word_count']].head()

print('Number of Words')
print(num_words)

# ===================================
# Number of Characters includes space                                                                
df['char_count'] = df['Sentence'].str.len()
num_char = df[['Sentence','char_count']].head()
print(num_char)

# =========
# Lowercase
df['Sentence'] = df['Sentence'].str.lower()
print(df)

# print(type(df['Sentence']))
# print(type(df['Sentence'][1]))

# =====================
# Removing punctuations
def remove_punctuations(df):
    for punctuation in string.punctuation:
        df = df.replace(punctuation, '')
    return df

# Applying the function to the DataFrame
df['Sentence'] = df['Sentence'].apply(remove_punctuations)
print(df['Sentence'].head())

# ================
# Removing Numbers
df['Sentence'] = df['Sentence'].str.replace('\d+','')
print(df['Sentence'].head())

# ==============================
# Number of Stop Words with NLTK 
# ==============================
from nltk.corpus import stopwords
stop = stopwords.words('english')
print('Stop Words:')
print(stop)

df['stopwords'] = df['Sentence'].apply(lambda x: len([x for x in x.split() if x in stop]))
stop_words = df[['Sentence','stopwords']].head()
print(stop_words)

# ===================                                                                     
# Removing Stop Words                                                                        
df['Sentence'] = df['Sentence'].apply(
    lambda x: " ".join(x for x in x.split() if x not in stop))

print(df['Sentence'].head())

# ===============
# Tokenizing text
# ==============================
# to split a sentence into words
from nltk.tokenize import word_tokenize

tokens = [word_tokenize(i) for i in my_lst]
for i in tokens:
    print(i)

# ========
# Stemming
# ===============
# Snowball Stemmer
from nltk.stem.snowball import SnowballStemmer

SnowballStemmer = SnowballStemmer('english')
stem_df = df['Sentence'][:6].apply(
    lambda x: " ".join([SnowballStemmer.stem(word) for word in x.split()]))

print('Stemmimg')
print(stem_df)

# =====================
# Number of final words                                                                              
df['word_count'] = df['Sentence'].apply(lambda x: len(str(x).split(" ")))
num_final_words = df[['Sentence','word_count']].head()
print(num_final_words)
















