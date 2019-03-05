#break down sentences into wordss
from nltk.tokenize import sent_tokenize, word_tokenize

textify="I am mr. Joseph a programmer based in Nigeria i deal with python, php and Csharp"
print(sent_tokenize(textify))
print(word_tokenize(textify))

for wod in word_tokenize(textify):
    print(wod)