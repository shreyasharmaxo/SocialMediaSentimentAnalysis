import json
from time import time
from Source.Reddit.RedditAPI import RedditAPI
from Source.Reddit.RedditSentimentAnalysis import RedditSentimentAnalysis
from Source.Politicians import politicians


def reddit_main():
    api = RedditAPI()
    analysis = RedditSentimentAnalysis()

    for p in politicians:
        query_headlines = api.fetch_headlines(p, 100)
        analyzed_headlines = analysis.sentiment_analysis(p, query_headlines)

        positive_headlines =[t for t in analyzed_headlines if t.get_sentiment() == 'positive']
        negative_headlines =[t for t in analyzed_headlines if t.get_sentiment() == 'negative']
        neutral_headlines  =[t for t in analyzed_headlines if t.get_sentiment() == 'neutral']

        print("Name of Politician: " + p + "\n")
        print("Positive Headline Count: {}".format(len(positive_headlines)))
        print("Negative Headline Count: {}".format(len(negative_headlines)))
        print("Neutral Headline Count: {}".format(len(neutral_headlines)))
        print("Total Headline Count: {}\n".format(len(analyzed_headlines)))

        if len(analyzed_headlines) > 0:
            print("Positive Headlines: {} %".format((len(positive_headlines) / len(analyzed_headlines)) * 100))
            print("Negative Headlines: {} %".format((len(negative_headlines) / len(analyzed_headlines)) * 100))
            print("Neutral Headlines: {} %\n".format((len(neutral_headlines) / len(analyzed_headlines)) * 100))

        print("------------------------------------------------------")

        analyzed_headlines_file = open('../../Data/RedditData/' + p + '_headlines.json', 'w')
        json.dump(list(analyzed_headlines), analyzed_headlines_file, default=to_json_version)
        analyzed_headlines_file.close()


def to_json_version(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__


if __name__ == "__main__":
    start_time = time()
    reddit_main()
    print("Time taken: %s minutes" % ((time() - start_time)/60))
