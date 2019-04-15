from time import time
from Source.Facebook.FacebookAPI import FacebookAPI
from Source.Facebook.FacebookSentimentAnalysis import FacebookSentimentAnalysis


def facebook_main():
    api = FacebookAPI()
    analysis = FacebookSentimentAnalysis()


if __name__ == "__main__":
    start_time = time()
    facebook_main()
    print("Time taken: %s minutes" % ((time() - start_time)/60))
