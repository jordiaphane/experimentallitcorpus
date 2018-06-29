import nltk.data
import re
import string
with open('C://Users//jbjb//Documents//DATA//weird corpus//extras//poundearly.txt', 'r', encoding='utf-8') as fuck:
	data=fuck.read().replace('\n', ' ')
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
print ('\n-----\n'.join(sent_detector.tokenize(data.strip())))
