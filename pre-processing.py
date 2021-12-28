# required libraries
import numpy as np
import pandas as pd
import re
import nltk
nltk.download()
import scapy
import string
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from read_pdf import train_resumes, test_resumes, job_req_str

train_data=[]
test_data=[]

single_words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

STOPWORDS = set(stopwords.words('english'))

# lemmatization
lemmatizer = WordNetLemmatizer()
wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}

# single words removing
def remove_single_word(text):
    resume = []
    for i in text.split():
        if i not in single_words:
            resume.append(i)
    return ' '.join(resume)

# lemmatize text
def lemmatize_words(text):
    pos_tagged_text = nltk.pos_tag(text.split())
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])

# Driver Funtion
def cleaned_text(text):
    # lowercasing all letters and removing single alphabet
    temp_text_1=remove_single_word(text.lower())
    # remove punctuations
    temp_text_2=temp_text_1.translate(str.maketrans('', '', string.punctuation))
    # Stopwords Removal
    temp_text_3=" ".join([word for word in str(temp_text_2).split() if word not in STOPWORDS])
    # Lemmatize Text
    temp_text_4=lemmatize_words(temp_text_3)
    temp_text_5 = re.sub('[^a-zA-Z0-9 \n\.]', '', temp_text_4)
    return(temp_text_5)


for resume in train_resumes:
    processed_str = cleaned_text(resume)
    train_data.append(processed_str)

for resume in test_resumes:
    lemma = cleaned_text(resume)
    test_data.append(lemma)

job_req = cleaned_text(job_req_str)

print(job_req)
