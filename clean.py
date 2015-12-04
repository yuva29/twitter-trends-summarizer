import sys
import os
import re
import string
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import pos_tag
				
def clean(path, filename):
	#print("Cleaning "+path)
	filename = CLEANED_DATA + filename.strip()
	WRITE_HANDLER = open(filename, 'w')
	tweets = dict()
	for line in open(path, 'r'):		
		line = re.sub(r'[.,"!]+', '', line, flags=re.MULTILINE) # removes the characters specified
		line = re.sub(r'^RT[\s]+', '', line, flags=re.MULTILINE) # removes RT
		line = re.sub(r'https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE) #remove link
		line = re.sub(r'[:]+', '', line, flags=re.MULTILINE)	
		line = filter(lambda x: x in string.printable, line) # filter non-ascii characers
		
		new_line = ""		
		for i in line.split(): # remove @ and #words, punctuataion
			if not i.startswith('@') and not i.startswith('#') and i not in string.punctuation:
				new_line+=i+" "	
		line = new_line			
		## Do sentence correction
		
		if(new_line in tweets):
			continue
		else:
			tweets[new_line] = 1
		if(len(new_line.strip())>0):
			WRITE_HANDLER.write(new_line + '\n\n')				
	return filename
			
DATA_FOLDER = sys.argv[1]
CLEANED_DATA = sys.argv[2]
for root, dirs, files in os.walk(DATA_FOLDER): # gets all the files from subfolders recrsively
	for name in files:
		absolute_path = os.path.join(root, name)
		if os.path.isfile(absolute_path) and name != ".DS_Store":
			filename = clean(absolute_path, name)
			#preprocess(filename, name) -- Call seperate tag code for this task
			
					

