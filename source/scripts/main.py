import json
from Twitter.TwitterMain import twitter_main
from Reddit.RedditMain import reddit_main
from scripts.scrape import get_info
from scripts.plot import twitter_sentiment_analysis, reddit_sentiment_analysis, sentiment_analysis

print("Enter the first name: ")
first_name = input()
print("Enter the last name: ")
last_name = input()
with open('../../data/query.json', 'w') as fp:
    json.dump(last_name, fp)
query = first_name + " " + last_name

print("Gathering Twitter data...")
twitter_main(query)
print("Gathering Reddit data...")
reddit_main(last_name)
print("Gathering Wikipedia data...")
get_info(first_name, last_name)
print("Gathering plot data...")
twitter_sentiment_analysis(query)
reddit_sentiment_analysis(query)
sentiment_analysis(query)
