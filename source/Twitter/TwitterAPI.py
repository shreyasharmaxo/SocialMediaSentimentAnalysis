import tweepy
from tweepy import OAuthHandler

'''
Class for creating and managing Twitter API
'''


class TwitterAPI(object):

    def __init__(self):
        # Gather keys
        consumer_key = 'IPnrrsNTBwmcYhq4vbZYU1bIq'
        consumer_secret = 'MsRRpxwC9vdyRlmVImtTc43jcVU8imNu9hhOCSjSSfiBSX18q3'
        access_token = '3433442513-T8xo9Jrha88HVZEvkZOo8iL9ijJNKvDseEWaUxg'
        access_token_secret = 'PCW6HNc0J39cTeswMY7qQq8Fw7cbm9ihPALO6PebmG0hH'

        # Authenticate
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except():
            print("Error: API authentication failed.")

    def fetch_tweets(self, topic, limit=100):
        try:
            query_tweets = self.api.search(q=topic, lang="en", result_type="recent", count=limit)
            return query_tweets

        except tweepy.TweepError as error:
            print("Error: " + str(error))
