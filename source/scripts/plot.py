import json
import matplotlib.pylab as plt

#  ------- Gathering data -------  #
path = 'C:/Users/gabeamaning/IdeaProjects/sp-19-cs242-final-project/data/twdata/'
with open(path + 'booker_tweets.json') as plot_data:
    data = json.load(plot_data)
with open(path + 'christie_tweets.json') as plot_data:
    data1 = json.load(plot_data)
with open(path + 'clinton_tweets.json') as plot_data:
    data2 = json.load(plot_data)
with open(path + 'cruz_tweets.json') as plot_data:
    data3 = json.load(plot_data)
with open(path + 'obama_tweets.json') as plot_data:
    data4 = json.load(plot_data)
with open(path + 'sanders_tweets.json') as plot_data:
    data5 = json.load(plot_data)
with open(path + 'trump_tweets.json') as plot_data:
    data6 = json.load(plot_data)

data = data + data1 + data2 + data3 + data4 + data5 + data6


#  ------- Determining which politicians get the most mentions -------  #
def count_mentions(query):
    count = 0
    for tweet in data:
        try:
            if query.upper() in tweet['rawText'].upper():
                count += 1
        except:
            continue
    return count


x = ["Booker", "Christie", "Clinton", "Cruz", "Obama", "Sanders", "Trump"]
y = [count_mentions(x[0]), count_mentions(x[1]), count_mentions(x[2]), count_mentions(x[3]), count_mentions(x[4]), count_mentions(x[5]), count_mentions(x[6])]
print(dict(zip(x, y)))
plt.bar(x, y)
plt.show()
