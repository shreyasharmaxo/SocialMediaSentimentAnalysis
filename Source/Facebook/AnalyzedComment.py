from Source.AnalyzedObject import AnalyzedObject


class AnalyzedComment(AnalyzedObject):

    def __init__(self, post_topic, raw_text, cleaned_text, polarity):
        super().__init__(raw_text, cleaned_text, polarity)
        self.topic = post_topic

    # Convert polarity value to sentiment
    def get_sentiment(self):
        if self.polarity > 0:
            return "positive"
        elif self.polarity < 0:
            return "negative"
        else:
            return "neutral"
