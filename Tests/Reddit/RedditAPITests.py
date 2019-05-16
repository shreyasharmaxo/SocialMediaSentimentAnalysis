import unittest
from Source.Reddit.RedditAPI import RedditAPI


class AnalysisTests(unittest.TestCase):

    def __init__(self, args):
        super(AnalysisTests, self).__init__(args)
        self.api = RedditAPI()

    def test_fetch_headlines(self):
        headlines = self.api.fetch_headlines("Donald Trump")
        self.assertTrue(len(headlines) > 0)
