import json
import matplotlib.pylab as plt

#  ------- Gathering data -------  #
path = 'C:/Users/gabeamaning/IdeaProjects/sp-19-cs242-final-project/data/'
with open(path + 'twdata/booker_tweets.json') as plot_data:
    booker_tweet_data = json.load(plot_data)
with open(path + 'twdata/christie_tweets.json') as plot_data:
    christie_tweet_data = json.load(plot_data)
with open(path + 'twdata/clinton_tweets.json') as plot_data:
    clinton_tweet_data = json.load(plot_data)
with open(path + 'twdata/cruz_tweets.json') as plot_data:
    cruz_tweet_data = json.load(plot_data)
with open(path + 'twdata/obama_tweets.json') as plot_data:
    obama_tweet_data = json.load(plot_data)
with open(path + 'twdata/sanders_tweets.json') as plot_data:
    sanders_tweet_data = json.load(plot_data)
with open(path + 'twdata/trump_tweets.json') as plot_data:
    trump_tweet_data = json.load(plot_data)

tweet_data = booker_tweet_data + christie_tweet_data + clinton_tweet_data + cruz_tweet_data + obama_tweet_data + sanders_tweet_data + trump_tweet_data

with open(path + 'oldFbData/fbdata.json', encoding="utf8") as plot_data:
    fbdata0 = json.load(plot_data)

with open(path + 'oldFbData/fbdata1.json', encoding="utf8") as plot_data:
    fbdata1 = json.load(plot_data)

fbdata = fbdata0 + fbdata1


#  ------- Analyzing Twitter Data -------  #
def twitter_sentiment_analysis(data, politician):
    table = dict([])
    table["Positive"] = 0
    table["Neutral"] = 0
    table["Negative"] = 0
    for tweet in data:
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
    print(politician + ": ")
    print(table)
    plt.title("Twitter Sentiment Analysis Data on " + politician)
    plt.bar(x_axis, y_axis)
    plt.show()


print("TWITTER SENTIMENT ANALYSIS")
twitter_sentiment_analysis(booker_tweet_data, "Booker")
twitter_sentiment_analysis(christie_tweet_data, "Christie")
twitter_sentiment_analysis(clinton_tweet_data, "Clinton")
twitter_sentiment_analysis(cruz_tweet_data, "Cruz")
twitter_sentiment_analysis(obama_tweet_data, "Obama")
twitter_sentiment_analysis(sanders_tweet_data, "Sanders")
twitter_sentiment_analysis(trump_tweet_data, "Trump")


#  ------- Analyzing Facebook Data -------  #
def facebook_sentiment_analysis(data):
    table = dict([])
    table["Positive"] = 0
    table["Negative"] = 0
    for comment in data:
        try:
            if comment["Positive"] > comment["Negative"]:
                table["Positive"] += 1
            elif comment["Positive"] < comment["Negative"]:
                table["Negative"] += 1
        except:
            continue
    x_axis = table.keys()
    y_axis = table.values()
    print(table)
    plt.title("Facebook Sentiment Analysis Data")
    plt.bar(x_axis, y_axis)
    plt.show()


print("FACEBOOK SENTIMENT ANALYSIS")
facebook_sentiment_analysis(fbdata)


#  ------- Analyzing All Data -------  #
#  ------- Sentiment Analysis on All Data -------  #
def sentiment_analysis(tw_data, fb_data):
    table = dict([])
    table["Positive"] = 0
    table["Negative"] = 0

    for tweet in tw_data:
        try:
            if tweet['polarity'] > 0:
                table["Positive"] += 1
            elif tweet['polarity'] < 0:
                table["Negative"] += 1
        except:
            continue

    for comment in fb_data:
        try:
            if comment["Positive"] > comment["Negative"]:
                table["Positive"] += 1
            elif comment["Positive"] < comment["Negative"]:
                table["Negative"] += 1
        except:
            continue
    x_axis = table.keys()
    y_axis = table.values()
    print(table)
    plt.title("Sentiment Analysis Data")
    plt.bar(x_axis, y_axis)
    plt.show()


print("COMBINED SENTIMENT ANALYSIS")
sentiment_analysis(tweet_data, fbdata)


#  ------- Determining which politicians get the most mentions -------  #
def count_mentions(query):
    count = 0
    for tweet in tweet_data:
        try:
            if query.upper() in tweet['rawText'].upper():
                count += 1
        except:
            continue
    for comment in fbdata:
        try:
            if query.upper() in comment['Comment'].upper():
                count += 1
        except:
            continue
    return count


x = ["Booker", "Christie", "Clinton", "Cruz", "Obama", "Sanders", "Trump"]
y = [count_mentions(x[0]), count_mentions(x[1]), count_mentions(x[2]), count_mentions(x[3]), count_mentions(x[4]), count_mentions(x[5]), count_mentions(x[6])]
print(dict(zip(x, y)))
plt.title("Politicians by mentions")
plt.bar(x, y)
plt.show()