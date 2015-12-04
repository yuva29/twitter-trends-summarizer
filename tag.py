import sys
import os
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import pos_tag

"""
Input : Folder containing all the cleaned data
Output : Tagged output for each file in input
"""

PREPROCESSED_DATA = "preprocessed/"
stop_words = dict()

def tag(path, filename):
	print("Tagging "+path)
	WRITE_HANDLER = open(PREPROCESSED_DATA + filename.strip() + "_features", 'w')
	for line in open(path, 'r'):	
		tokens = line.split()
		if(len(tokens) == 0):
			continue
		tags = pos_tag(tokens) # tag
			
		features = list()
		for token in tags:
			tok = token[0]
			tag = token[1]
			if tok.lower() not in stop_words:
				features.append(tok+":"+tag)				
		if(len(features)>0):
			WRITE_HANDLER.write(str(features)+'\n\n')
		else: ## EMPTY lines
			WRITE_HANDLER.write('\n\n')
			
def get_stop_words():
	if(len(stop_words)>0):
		return stop_words		
	stop = stopwords.words('english') ## Stop chars
	for s in stop:
		stop_words[s] = 1
	return stop_words

CLEANED_DATA_DIR = sys.argv[1]
get_stop_words()	
for root, dirs, files in os.walk(CLEANED_DATA_DIR): # gets all the files from subfolders recrsively
	for name in files:
		absolute_path = os.path.join(root, name)
		if os.path.isfile(absolute_path) and name != ".DS_Store":
			tag(absolute_path, name)		
			
