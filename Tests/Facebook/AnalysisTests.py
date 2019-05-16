import unittest
from Source.Facebook.FacebookSentimentAnalysis import FacebookSentimentAnalysis


class AnalysisTests(unittest.TestCase):

    def __init__(self, args):
        super(AnalysisTests, self).__init__(args)
        self.analysis = FacebookSentimentAnalysis()

    def test_polarity (self):
        # Positive Sentiment
        positive_simple = "That election was really good."
        # Negative Sentiment
        negative_simple = "That election was so bad!"
        # Neutral Sentiment
        neutral_simple = "I have no opinion of that election."

        self.assertTrue(FacebookSentimentAnalysis.polarity_of_comment(positive_simple) > 0)
        self.assertTrue(FacebookSentimentAnalysis.polarity_of_comment(negative_simple) < 0)
        self.assertTrue(FacebookSentimentAnalysis.polarity_of_comment(neutral_simple) == 0)
