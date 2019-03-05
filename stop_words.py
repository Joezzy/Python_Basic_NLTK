from nltk.corpus import stopwords
from nltk.tokenize import  word_tokenize

textify="I am mr. Joseph a programmer based in Nigeria i deal with python, php and Csharp"
stop_wodz=set(stopwords.words("english"))


words=word_tokenize(textify)

filtered_sentence=[wod for wod in words if not wod in stop_wodz]
print(filtered_sentence)

# this is the broking down process of the above process
# filtered_sentence=[]

# for wo in words:
#     if wo not in stop_wodz:
#         filtered_sentence.append(wo)
# print(filtered_sentence)
