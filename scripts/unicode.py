from nltk.tokenize import sent_tokenize, word_tokenize
import ftfy
with open('C://Users//jbjb//Documents//DATA//weird corpus//ulysses.txt', 'r', encoding='utf-8') as fuck:
	data=fuck.read().replace('\n-----\n', '')
cool = ftfy.fix_text(str(data))
print (cool)
