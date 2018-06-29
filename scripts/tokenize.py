from nltk.tokenize import sent_tokenize, word_tokenize

with open ('C:\\Users\\jbjb\\Documents\\DATA\\weird corpus\\finneganswake.txt', 'r', encoding='utf-8') as file:
	f = file.read()
reri = sent_tokenize(f)
rari = [word_tokenize(rari) for rari in sent_tokenize(f)]
print (rari)
