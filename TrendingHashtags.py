import tweepy
import time, sys 

import warnings
warnings.filterwarnings("ignore")

ACCESS_TOKEN = "288597754-rJGehtrfHILQLoIzdhUjnNhbqkpxPvzrBOUaJQGl"
ACCESS_TOKEN_SECRET = "BEwxd4UbWgVBWFz3tGsOdXYEbDNT5bK7XQNKrdcmdjML7"
CONSUMER_KEY = "TsD81Kd8J93gtVcsPRwfmDXFh"
CONSUMER_SECRET = "daPxbl9oexqmsBoEp6nZ764Ro0j0jUE9pzSMXIT4xoVCnUi8ff"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

trending = api.trends_place(1)

#Trending topics
topics = [x['name'] for x in trending[0]['trends']]
for topic in topics:
	print(topic.encode('utf-8').strip())
	
# Trending hash tags
#hashtags = [x['name'] for x in trending[0]['trends'] if x['name'].startswith('#')]
#print hashtags
