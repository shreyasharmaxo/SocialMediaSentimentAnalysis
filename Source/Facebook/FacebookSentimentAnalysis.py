from textblob import TextBlob
from Source.Facebook.AnalyzedComment import AnalyzedComment


class FacebookSentimentAnalysis(object):

    def sentiment_analysis(self, post_topic, query_comments):
        analyzed_comments = []

        for comment in query_comments:
            raw_text = comment
            cleaned_text = self.clean_comment(raw_text)

            polarity = self.polarity_of_comment(cleaned_text)

            analyzed_comment = AnalyzedComment(post_topic, raw_text, cleaned_text, polarity)

            if analyzed_comment not in analyzed_comments:
                analyzed_comments.append(analyzed_comment)

        return analyzed_comments

    # Remove new line characters
    @staticmethod
    def clean_comment(comment):
        return comment.replace('\n', ' ')

    # Analyze comment for polarity varying from -1 (negative) to 1 (positive)
    @staticmethod
    def polarity_of_comment(comment):
        analysis = TextBlob(comment)
        return analysis.polarity
