#brings out root word or part of speech version of the word
from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()

print (lemmatizer.lemmatize("cats"))
print (lemmatizer.lemmatize("better", pos="a"))