#import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from Source.Reddit.AnalyzedHeadline import AnalyzedHeadline


class RedditSentimentAnalysis(object):

    # Returns a list of analyzed headlines after cleaning text
    def sentiment_analysis(self, headline_topic, query_headlines):
        analyzed_headlines = []

        for headline in query_headlines:
            raw_text = headline
            polarity = self.polarity_of_headline(raw_text)

            analyzed_headline = AnalyzedHeadline(headline_topic, raw_text, raw_text, polarity)

            if analyzed_headline not in analyzed_headlines:
                analyzed_headlines.append(analyzed_headline)

        return analyzed_headlines

    # Analyze headline for polarity varying from -1 (negative) to 1 (positive)
    @staticmethod
    def polarity_of_headline(headline):
        sia = SentimentIntensityAnalyzer()
        polarity = sia.polarity_scores(headline)
        return polarity
