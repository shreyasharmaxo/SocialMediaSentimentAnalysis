import unittest
from Source.Facebook.FacebookAPI import FacebookAPI


class AnalysisTests(unittest.TestCase):

    def __init__(self, args):
        super(AnalysisTests, self).__init__(args)
        self.api = FacebookAPI()

    def test_fetch_tweets(self):
        comments = self.api.fetch_fake_comments()
        self.assertTrue(len(comments) > 0)
