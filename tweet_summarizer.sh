current_dir="$(pwd)"
tweet_directory="$current_dir/$1*"
summary_directory="$current_dir/$2"
tweet_feat_directory="$current_dir/$3"
summary_feat_directory="$current_dir/$4"
predicte_dir=$5 
# echo "$tweet_directory ----"
for f in $tweet_directory
do
	# echo "$f"
	input_tweets="input_tweets.txt"
	input_tweets_features="input_tweets_feat.txt"

	cp $f $input_tweets
	tweet_file_name=$(basename "$f")
	summary_file="$summary_directory$tweet_file_name"
	summary_file="$summary_file.txt"
	# echo "$summary_file"
	# echo "$f"
	

	tweet_feat_file="$tweet_feat_directory$tweet_file_name"
	feat="_features"
	tweet_feat_file="$tweet_feat_file$feat"
	# echo "$tweet_feat_file"

	summary_feat_file="$summary_feat_directory$tweet_file_name"
	tok="_token.txt"
	summary_feat_file="$summary_feat_file$tok"
	# echo $summary_feat_file

	cp $tweet_feat_file $input_tweets_features
	
	#echo "<<<<<<     $tweet_file_name       >>>>>>>"
	#python tweet_summarizer.py $input_tweets $input_tweets_features
	#echo "-------------------------------------------------------------------"

	cat $summary_file >> $input_tweets
	cat $summary_feat_file >> $input_tweets_features
	python tweet_summarizer.py $input_tweets $input_tweets_features > $5/$tweet_file_name
	#echo "-------------------------------------------------------------------"	


done
