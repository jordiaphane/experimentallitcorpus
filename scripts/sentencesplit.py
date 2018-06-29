from nltk.tokenize import word_tokenize
import re
import string
with open('C://Users//jbjb//Documents//DATA//weird corpus//finneganswake.txt', 'r', encoding='utf-8') as fuck:
	data=fuck.read().replace('\n-----\n', '\n')
newdata = word_tokenize(data, preserve_line=True)
print (newdata)