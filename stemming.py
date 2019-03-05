# Its like trimming a morphological word to its root word
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

pstemmer=PorterStemmer()

example_text=["Joseph","Josepher","Josephing","Josephed","Josephly"]

# for wod in example_text:
#     print(pstemmer.stem(wod))

texify="this is to josephed us in all josephing we will be doing josephly by all josepher wjo knows joseph"
wod=word_tokenize(texify)

for wd in wod:
    print(pstemmer.stem(wd))
