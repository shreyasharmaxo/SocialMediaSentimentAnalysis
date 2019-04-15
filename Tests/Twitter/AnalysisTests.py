import unittest
from Source.Twitter.TwitterSentimentAnalysis import TwitterSentimentAnalysis


class AnalysisTests(unittest.TestCase):

    def __init__(self, args):
        super(AnalysisTests, self).__init__(args)
        self.analysis = TwitterSentimentAnalysis()

    def test_polarity (self):
        # Positive Sentiment
        positive_simple = "Donald Trump is a wonderful person!"
        # Negative Sentiment
        negative_simple = "Donald Trump is a horrible person!"
        # Neutral Sentiment
        neutral_simple = "I have no opinion of Donald Trump."

        self.assertTrue(TwitterSentimentAnalysis.polarity_of_tweet(positive_simple) > 0)
        self.assertTrue(TwitterSentimentAnalysis.polarity_of_tweet(negative_simple) < 0)
        self.assertTrue(TwitterSentimentAnalysis.polarity_of_tweet(neutral_simple) == 0)
