import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
import sys




stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def calculateSimilarity():
	sum = 0
	maxVal = 0
	actual = open(sys.argv[1], "r")
	for a in actual:
		predicted = open(sys.argv[2], "r")
		for p in predicted:
			temp = cosine_sim(a,p)
			maxVal = max(temp, maxVal)
			sum += temp
		predicted.close()
	actual.close()
	print("avg" + str(sum/16))
	print("max" + str(maxVal))


calculateSimilarity()