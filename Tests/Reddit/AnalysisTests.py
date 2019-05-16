import unittest
from Source.Reddit.RedditSentimentAnalysis import RedditSentimentAnalysis


class AnalysisTests(unittest.TestCase):

    def __init__(self, args):
        super(AnalysisTests, self).__init__(args)
        self.analysis = RedditSentimentAnalysis()

    def test_polarity (self):
        # Positive Sentiment
        positive_simple = "Donald Trump built a good wall!!"
        # Negative Sentiment
        negative_simple = "Donald Trump is a horrible leader"
        # Neutral Sentiment
        neutral_simple = "I din't know.."

        self.assertTrue(RedditSentimentAnalysis.polarity_of_headline(positive_simple) > 0)
        self.assertTrue(RedditSentimentAnalysis.polarity_of_headline(negative_simple) < 0)
        self.assertTrue(RedditSentimentAnalysis.polarity_of_headline(neutral_simple) == 0)
