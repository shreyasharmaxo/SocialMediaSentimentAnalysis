import json
import matplotlib.pylab as plt

#  ------- Gathering data -------  #
path = 'C:/Users/gabeamaning/IdeaProjects/sp-19-cs242-final-project/data/'
with open(path + 'TwitterData/tweets.json') as plot_data:
    tweet_data = json.load(plot_data)

with open(path + 'RedditData/headlines.json') as plot_data:
    reddit_data = json.load(plot_data)


#  ------- Analyzing Twitter Data -------  #
def twitter_sentiment_analysis(politician):
    print("TWITTER SENTIMENT ANALYSIS")
    table = dict([])
    table["Positive"] = 0
    table["Negative"] = 0
    table["Neutral"] = 0

    for tweet in tweet_data:
        try:
            if tweet['polarity'] > 0:
                table["Positive"] += 1
            elif tweet['polarity'] < 0:
                table["Negative"] += 1
            else:
                table["Neutral"] += 1
        except:
            continue
    x_axis = table.keys()
    y_axis = table.values()
    print(table)
    plt.title("Twitter Sentiment Analysis Data on " + politician)
    plt.bar(x_axis, y_axis)
    plt.gcf().savefig('../assets/twitter_plot_data.png')


# twitter_sentiment_analysis(query)


#  ------- Analyzing Reddit Data -------  #
def reddit_sentiment_analysis(politician):
    print("REDDIT SENTIMENT ANALYSIS")
    table = dict([])
    table["Positive"] = 0
    table["Negative"] = 0
    table["Neutral"] = 0
    for post in reddit_data:
        try:
            if post["compound"] > 0:
                table["Positive"] += 1
            elif post["compound"] < 0:
                table["Negative"] += 1
            else:
                table["Neutral"] += 1
        except:
            continue
    x_axis = table.keys()
    y_axis = table.values()
    print(table)
    plt.title("Reddit Sentiment Analysis Data on " + politician)
    plt.bar(x_axis, y_axis)
    plt.gcf().savefig('../assets/reddit_plot_data.png')


# reddit_sentiment_analysis(query)


#  ------- Analyzing All Data -------  #
#  ------- Sentiment Analysis on All Data -------  #
def sentiment_analysis(politician):
    print("COMBINED SENTIMENT ANALYSIS")
    table = dict([])
    table["Positive"] = 0
    table["Negative"] = 0
    table["Neutral"] = 0

    for tweet in tweet_data:
        try:
            if tweet['polarity'] > 0:
                table["Positive"] += 1
            elif tweet['polarity'] < 0:
                table["Negative"] += 1
            else:
                table["Neutral"] += 1
        except:
            continue

    for post in reddit_data:
        try:
            if post["compound"] > 0:
                table["Positive"] += 1
            elif post["compound"] < 0:
                table["Negative"] += 1
            else:
                table["Neutral"] += 1
        except:
            continue
    x_axis = table.keys()
    y_axis = table.values()
    print(table)
    plt.title("Sentiment Analysis Data on " + politician)
    plt.bar(x_axis, y_axis)
    plt.gcf().savefig('../assets/combined_plot_data.png')


# sentiment_analysis(query)
