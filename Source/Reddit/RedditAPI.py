import praw
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')


class RedditAPI(object):

    def __init__(self):
        # Authenticate
        self.reddit = praw.Reddit(client_id='qQo3bYJL6q7cgA',
                                  client_secret='polADCr-A1NF5PIbIRr5lHDuQv4',
                                  user_agent='shreyasharmaxo')

    def fetch_headlines(self, topic, limit=None):
        headlines = set()

        for submission in self.reddit.subreddit('politics').new(limit=limit):
            if topic.upper() in submission.title.upper():
                headlines.add(submission.title)

        return headlines
