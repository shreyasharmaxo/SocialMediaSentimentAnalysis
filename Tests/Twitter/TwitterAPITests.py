import unittest
from Source.Twitter.TwitterAPI import TwitterAPI


class AnalysisTests(unittest.TestCase):

    def __init__(self, args):
        super(AnalysisTests, self).__init__(args)
        self.api = TwitterAPI()

    def test_fetch_tweets(self):
        tweets = self.api.fetch_tweets("Donald Trump", 100)
        self.assertTrue((len(tweets) > 0) & (len(tweets) < 100))
