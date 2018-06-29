from nltk.tokenize import WhitespaceTokenizer
import string
with open('C://Users//jbjb//Documents//DATA//weird corpus//agape.txt', 'r', encoding='utf-8') as fuck:
	data=fuck.read().replace('\n-----\n', '\n')
ace = list(WhitespaceTokenizer().span_tokenize(data))
print (ace)