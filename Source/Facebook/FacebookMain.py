from time import time
from Source.Facebook.FacebookAPI import FacebookAPI
from Source.Facebook.FacebookSentimentAnalysis import FacebookSentimentAnalysis


def facebook_main():
    api = FacebookAPI()
    analysis = FacebookSentimentAnalysis()

    query_comments = api.fetch_fake_data()
    analyzed_comments = analysis.sentiment_analysis("United States presidential election 2016", query_comments)
    print(analyzed_comments)


if __name__ == "__main__":
    start_time = time()
    facebook_main()
    print("Time taken: %s minutes" % ((time() - start_time)/60))
