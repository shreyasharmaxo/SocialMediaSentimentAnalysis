from google.cloud import language
from Source.Facebook.AnalyzedComment import AnalyzedComment


class FacebookSentimentAnalysis(object):

    def sentiment_analysis(self, post_topic, query_comments):
        analyzed_comments = []

        client = language.LanguageServiceClient()

        for comment in query_comments:
            raw_text = comment
            cleaned_text = self.clean_comment(raw_text)

            document = language.types.Document(
                content=cleaned_text,
                type=language.enums.Document.Type.PLAIN_TEXT)

            sentiment = client.analyze_sentiment(document).document_sentiment

            analyzed_comment = AnalyzedComment(raw_text, cleaned_text, sentiment.score, sentiment.magnitude, post_topic)

            if analyzed_comment not in analyzed_comments:
                analyzed_comments.append(analyzed_comment)

        return analyzed_comments

    # Remove new line characters
    @staticmethod
    def clean_comment(comment):
        return comment.replace('\n', ' ')
