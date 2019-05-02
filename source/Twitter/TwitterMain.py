import json
from time import time
from Twitter.TwitterAPI import TwitterAPI
from Twitter.TwitterSentimentAnalysis import TwitterSentimentAnalysis


def twitter_main(query):
    api = TwitterAPI()
    analysis = TwitterSentimentAnalysis()

    query_tweets = api.fetch_tweets(query, 100)
    analyzed_tweets = analysis.sentiment_analysis(query, query_tweets)

    analyzed_tweets_file = open('../../Data/TwitterData/tweets.json', 'w')
    json.dump(list(analyzed_tweets), analyzed_tweets_file, default=to_json_version)
    analyzed_tweets_file.close()


def to_json_version(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__


'''
if __name__ == "__main__":
    start_time = time()
    twitter_main(qry)
    print("Time taken: %s minutes" % ((time() - start_time)/60))
'''
