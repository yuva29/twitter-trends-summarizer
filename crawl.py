# Import the necessary methods from tweepy library
import sys

from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from tweepy import TweepError

import warnings
warnings.filterwarnings("ignore")

# Variables that contains the user credentials to access Twitter API 
# # keys from  "Twitter Tweet Summarization" app
access_token = "288597754-rJGehtrfHILQLoIzdhUjnNhbqkpxPvzrBOUaJQGl"
access_token_secret = "BEwxd4UbWgVBWFz3tGsOdXYEbDNT5bK7XQNKrdcmdjML7"
consumer_key = "TsD81Kd8J93gtVcsPRwfmDXFh"
consumer_secret = "daPxbl9oexqmsBoEp6nZ764Ro0j0jUE9pzSMXIT4xoVCnUi8ff"

DATA_FOLDER = sys.argv[1]

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print (status)

def query_through_stream(topic):
    stream = Stream(auth, l)
    stream.filter(track=[topic])

def query_through_search(query):
	TOPIC_DATA_HANDLER = open(DATA_FOLDER + query, 'w')
	api = API(auth)
	
	tweets = dict()
	# # Initialization ## 
	max_tweets = 500
	tweet_count = 0
	max_id = -1
	since_id = None
	tweet_per_query = 100
	
	# print("Downloading tweets for query : "+query)
	while tweet_count < max_tweets:
		try:
			if (max_id <= 0):
				if (not since_id):
					new_tweets = api.search(q=query, count=tweet_per_query, lang="en", result_type="mixed", locale="en")
				else:
					new_tweets = api.search(q=query, count=tweet_per_query, since_id=since_id, lang="en", result_type="mixed", locale="en")
			else:
				if (not since_id):
					new_tweets = api.search(q=query, count=tweet_per_query, max_id=str(max_id - 1), lang="en", result_type="mixed", locale="en")
				else:
					new_tweets = api.search(q=query, count=tweet_per_query, max_id=str(max_id - 1), since_id=since_id, lang="en", result_type="mixed", locale="en")
			if not new_tweets:
				print("No more tweets found")
				break
			tweet_id_iter = None
			for tweet in new_tweets:
				# json_tweet = jsonpickle.encode(tweet._json, unpicklable=False)
				if(tweet.user.followers_count > 200 and tweet.text not in tweets):
					tweet_text = (tweet.text).encode('utf-8').strip()
					tweet_text = tweet_text.replace('\n', " ")
					
					tweets[tweet.text] = 1  # # for duplicate identification
					
					TOPIC_DATA_HANDLER.write(tweet_text + '\n\n')
					tweet_count += 1
					if(tweet_id_iter):
						tweet_id_iter = min(tweet_id_iter, tweet.id)
					else:
						tweet_id_iter = tweet.id
					if(tweet_count == max_tweets):
						break					
			# tweet_count += len(new_tweets)
			# print("Downloaded {0} tweets".format(tweet_count))
			# max_id = new_tweets[-1].id
			max_id = tweet_id_iter
		except TweepError as e:
			print("some error : " + str(e))
			break
	
def isEnglish(s):
    try:
        s.decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
        
if __name__ == '__main__':
    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    TOPICS = sys.argv[1]
    for topic in open(TOPICS, 'r'):
    	if(isEnglish(topic)):    		
	    	query_through_search(topic.encode('utf-8').strip())
    	
    # query_through_stream("Scandal")
    

	
	
