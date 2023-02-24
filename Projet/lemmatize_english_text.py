import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from pprint import pprint

#nltk.download('omw-1.4')
#nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def lemmatize_print(words) :
	a = []
	tokens = word_tokenize(words)
	for token in tokens:
		lemmatized_word = lemmatizer.lemmatize(token)
		a.append(lemmatized_word)
		return ((a[i] + " : " + tokens[i]) for i in range(len(a)))

res = ""

with open('EMEA.en-fr.en.res', 'w') as file2:
	with open('EMEA.en-fr.en', 'r') as file:
		data = file.read().split('\n')
		
		for i in range(len(data)):
			text = lemmatize_print(data[i])
			for j in text:
				res += j + '\n'
	
	file2.write(res)
