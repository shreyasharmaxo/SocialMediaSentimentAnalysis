import praw
import json
import seaborn as sns
#import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sns.set(style='darkgrid', context='talk', palette='Dark2')


reddit = praw.Reddit(client_id='qQo3bYJL6q7cgA',
                     client_secret='polADCr-A1NF5PIbIRr5lHDuQv4',
                     user_agent='shreyasharmaxo')

headlines = set()

for submission in reddit.subreddit('politics').new(limit=None):
    headlines.add(submission.title)

sia = SentimentIntensityAnalyzer()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

with open('../../Data/RedditData/politicalheadlines.json', 'w') as fp:
    json.dump(results, fp)
