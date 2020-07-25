from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from os import path, mkdir
import io
import glob

#from webcrawler import queries

#this python file facilitates the use of Scikit Learn libraries to extract features in 2 ways
#through vectorizing (ie. Bag of Words) and also TF-IDF techniques

vectorizer = CountVectorizer()
wiki = open("./dataset/fall/Autumn - Wikipedia.txt", encoding="utf-8")
text = wiki.read()
#print(text)

#WATCH THIS https://www.youtube.com/watch?v=7YacOe4XwhY5

corpus = [
    text,
]
x = vectorizer.fit_transform(corpus)
print(x)

analyze = vectorizer.build_analyzer()
print(analyze("this is a text document to analyze"))

print(vectorizer.get_feature_names())

print(x.toarray())

print(x)