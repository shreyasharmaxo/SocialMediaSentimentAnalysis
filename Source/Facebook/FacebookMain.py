import json
from time import time
from Source.Facebook.FacebookAPI import FacebookAPI
from Source.Facebook.FacebookSentimentAnalysis import FacebookSentimentAnalysis


def facebook_main():
    api = FacebookAPI()
    analysis = FacebookSentimentAnalysis()

    query_tweets = api.fetch_fake_comments()
    analyzed_comments = analysis.sentiment_analysis("election", query_tweets)

    positive_comments =[t for t in analyzed_comments if t.get_sentiment() == 'positive']
    negative_comments =[t for t in analyzed_comments if t.get_sentiment() == 'negative']
    neutral_comments  =[t for t in analyzed_comments if t.get_sentiment() == 'neutral']

    print("Facebook Post Topic: 2016 Election: \n")
    print("Positive Comment Count: {}".format(len(positive_comments)))
    print("Negative Comment Count: {}".format(len(negative_comments)))
    print("Neutral Comment Count: {}".format(len(neutral_comments)))
    print("Total Comment Count: {}\n".format(len(analyzed_comments)))

    print("Positive Comments: {} %".format((len(positive_comments) / len(analyzed_comments)) * 100))
    print("Negative Comments: {} %".format((len(negative_comments) / len(analyzed_comments)) * 100))
    print("Neutral Comments: {} %\n".format((len(neutral_comments) / len(analyzed_comments)) * 100))
    print("------------------------------------------------------")

    analyzed_comments_file = open('../../Data/FacebookData/analyzed_election_comments.json', 'w')
    json.dump(list(analyzed_comments), analyzed_comments_file, default=to_json_version)
    analyzed_comments_file.close()


def to_json_version(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__


if __name__ == "__main__":
    start_time = time()
    facebook_main()
    print("Time taken: %s minutes" % ((time() - start_time)/60))
