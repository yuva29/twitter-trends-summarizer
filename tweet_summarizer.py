from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import pos_tag
from nltk import wordnet as wn
from nltk.wsd import lesk
import string
import argparse
import operator

# Takes a text as an input, removes stop words and punctuation marks from it 
# and returns a set of stemmed version of the remaining words.
def getStemmedForm(text,stemmer_obj):
	stop = stopwords.words('english')
	for i in string.punctuation:
		stop.append(i)
	remainder = [i for i in word_tokenize(text.lower()) if i not in stop]
	# return remainder
	stemmed_remainder = set()
	for w in remainder:
		x=stemmer_obj.stem(w)
		# print(w+"\t"+x)
		stemmed_remainder.add(x)
	return stemmed_remainder


# Only selects the features which are Nouns excluding proper nouns, verbs, adverbs & adjectives
# returns a dictionary of feat:pos_tag
def removeUnwantedFeatures(tweet_features):
	featues_tag = ['FW','JJ','JJR','JJS','NN','NNS','RB','RBR','RBS','VB','VBD','VBG','VBN','VBP','VBZ','WRB']
	reduced_features = {}
	for feature in tweet_features:
		token = feature.split(":")
		# if token[1] in featues_tag:
		# 	reduced_features[token[0]] = token[1]
		reduced_features[token[0]] = token[1]
	return reduced_features

def penn_to_wn(tag):
    if tag.startswith('J') or tag.startswith('W'):
        return 'a' #ADJECTIVE are represented as 'a' in WordNet
    elif tag.startswith('N'):
        return 'n' #NOUN are represented as 'n' in WordNet
    elif tag.startswith('R'):
        return 'r' #ADVERB are represented as 'r' in WordNet
    elif tag.startswith('V'): 
        return 'v' #VERB are represented as 'v' in WordNet
    return None

stemmer = PorterStemmer()
parser = argparse.ArgumentParser()
parser.add_argument("cleaned_data")
parser.add_argument("processed_data")
args = parser.parse_args()
cleaned_data = open( args.cleaned_data, "r+")
processed_data = open( args.processed_data, "r+")
index=0
tweet_map = {}
tweet_weights = {}
max_weight = -1
max_tweet = ""
for tweet in cleaned_data:
	tweet = tweet.strip()
	if not tweet:
		processed_data.readline()
		continue 
	else:
		tweet_map[index] = tweet
		weight=0
		tweet_set = getStemmedForm(tweet,stemmer)
		tweet_features_string = processed_data.readline().strip()
		if not tweet_features_string:
			continue
		else:
			tweet_features = eval(tweet_features_string)
			reduced_features = removeUnwantedFeatures(tweet_features)
			# print("*****")
			# print(tweet)
			# print(tweet_features)
			# print(reduced_features)
			# print("*****")
			for feature,feature_pos_tag in reduced_features.items():
				# print("Curren feat:"+feature+" "+feature_pos_tag)
				feature_synset = lesk(tweet, feature, penn_to_wn(feature_pos_tag))
				if feature_synset is not None:
					
					feature_meaning = feature_synset.definition()
					feature_meaning_set = getStemmedForm(feature_meaning,stemmer)
					
					# print(feature_synset.definition())
					# print(tweet_set)
					# print(feature_meaning_set)
					# print(set.intersection(tweet_set,feature_meaning_set))
					weight+=len(set.intersection(tweet_set,feature_meaning_set))
					# print("---")
		# print("Weight:"+str(weight))
		if weight > max_weight:
			max_weight = weight
			max_tweet = tweet
		tweet_weights[index]=weight
		index+=1
sorted_tweet_weights = sorted(tweet_weights.items(), key=operator.itemgetter(1), reverse=True)
# print(sorted_tweet_weights)
count = 0
for items in sorted_tweet_weights:
	print(tweet_map[items[0]])
	count+=1
	if(count == 4):
		break;

# print("Max:"+str(max_weight)+" tweet:"+str(max_tweet))

# Elvis Costello said writing about music is like dancing about architecture and I feel like that's also Bill Walton's a
# Tropical gear only for the tropics Buy some island stuff I wanna see u rocking something from the Bill Walton collection
# Luke Walton trying to win 16th in a row Dad Bill won 93 in a row on UCLA frosh &amp; varsity teams before his first loss as player in college
# hope this guy can stay healthy he's becoming the modern day Bill Walton I j s
