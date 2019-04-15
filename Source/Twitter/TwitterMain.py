import json
from time import time
from Source.Twitter.TwitterAPI import TwitterAPI
from Source.Twitter.TwitterSentimentAnalysis import TwitterSentimentAnalysis


def twitter_main():
    api = TwitterAPI()
    analysis = TwitterSentimentAnalysis()

    query_tweets = api.fetch_tweets("Barack Obama", 100)
    analyzed_tweets = analysis.sentiment_analysis("Barack Obama", query_tweets)

    positive_tweets = [t for t in analyzed_tweets if t.get_sentiment() == 'positive']
    negative_tweets = [t for t in analyzed_tweets if t.get_sentiment() == 'negative']
    neutral_tweets  = [t for t in analyzed_tweets if t.get_sentiment() == 'neutral']

    print("Positive Tweet Count: {}".format(len(positive_tweets)))
    print("Negative Tweet Count: {}".format(len(negative_tweets)))
    print("Neutral Tweet Count: {}".format(len(neutral_tweets)))
    print("Total Tweet Count: {}\n".format(len(analyzed_tweets)))

    print("Positive tweets: {} %".format((len(positive_tweets)/len(analyzed_tweets))*100))
    print("Negative tweets: {} %".format((len(negative_tweets)/len(analyzed_tweets))*100))
    print("Neutral tweets: {} %\n".format((len(neutral_tweets)/len(analyzed_tweets))*100))

    analyzed_tweets_file = open('../../Data/TwitterData/obama_tweets.json', 'w')
    json.dump(list(analyzed_tweets), analyzed_tweets_file, default=to_json_version)
    analyzed_tweets_file.close()


def to_json_version(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__


if __name__ == "__main__":
    start_time = time()
    twitter_main()
    print("Time taken: %s minutes" % ((time() - start_time)/60))
