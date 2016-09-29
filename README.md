Summaries will greatly help the user in understanding “why the topic is trending”. We have proposed an algorithm which automatically generates summaries for trending topics/hashtags based on tweets and it's related news article.

Requirements: 
```
1. pip install tweepy
2. pip install nltk
```
	 
1. `TrendingHashtags.py`
	Collect currently trending hashtags. 
	To run: TrendingHashtags.py > hashtags.txt
2. `crawl.py`
	Crawls Twitter for the trends in hashtags.txt
	To run: python crawl.py hashtags.txt path_to_store_tweets
	Output: will create a file for tweets crawled for each trending topic/hashtag.
3. `clean.py`
	Removes twitter specific stop words from the data
	To run: python clean.py path_to_tweets_folder path_to_store_tweets
	Output: a file for tweets pertaining to each topic/hashtag
4. `tag.py`
	Pre-process the data
	To run: python tag.py path_to_cleaned_data path_to_preprocess_data
	Output: a file for tweets pertaining to each topic/hashtag
5. `./tweet_summarizer.sh path_to_clean_tweets path_to_news_articles path_to_tagged_tweets path_to_tagged_news_articles path_to_predicted_folder`
	Output: Summary will be generated for the trending topics/hashtags in predicted folder
6. `cosine_similarity.py`
	Calculate cosine similarity between human picked and algorithm generated summary
	To run: python cosine_similarity.py path_to_actual_file path_to_predicted_file
	Output: average and max similarity
7. `semantic_similarity.py`
	Calculate semantic similarity between human picked and algorithm generated summary
	To run: python semantic_similarity.py path_to_actual_file path_to_predicted_file
	Output: average and max similarity
