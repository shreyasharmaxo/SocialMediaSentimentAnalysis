from Source.AnalyzedObject import AnalyzedObject


class AnalyzedComment(AnalyzedObject):

    def __init__(self, raw_text, cleaned_text, polarity, magnitude, post_topic):
        super().__init__(raw_text, cleaned_text, polarity)
        self.post_topic = post_topic
        self.magnitude = magnitude

    # Convert polarity value to sentiment
    def get_sentiment(self):
        if self.polarity > 0:
            return "positive"
        elif self.polarity < 0:
            return "negative"
        else:
            return "neutral"
