import re
from textblob import TextBlob
from Source.Twitter.AnalyzedTweet import AnalyzedTweet


class TwitterSentimentAnalysis(object):

    # Returns a list of analyzed tweets after cleaning text
    def sentiment_analysis(self, query, query_tweets):
        analyzed_tweets = []

        for tweet in query_tweets:
            raw_text = tweet.text
            cleaned_text = self.clean_tweet(raw_text)
            polarity = self.polarity_of_tweet(cleaned_text)

            analyzed_tweet = AnalyzedTweet(query, raw_text, cleaned_text, polarity)

            if analyzed_tweet not in analyzed_tweets:
                analyzed_tweets.append(analyzed_tweet)

        return analyzed_tweets

    # Remove hyperlinks and special characters
    @staticmethod
    def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+) | ([^0-9A-Za-z \t]) | (\w+:\ / \ / \S+)", " ", tweet).split())

    # Analyze tweet for polarity varying from -1 (negative) to 1 (positive)
    @staticmethod
    def polarity_of_tweet(tweet):
        analysis = TextBlob(tweet)
        return analysis.polarity
