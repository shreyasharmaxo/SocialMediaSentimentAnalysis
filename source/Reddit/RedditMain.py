import seaborn as sns
import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import json
# nltk.download('vader_lexicon')
sns.set(style='darkgrid', context='talk', palette='Dark2')


def reddit_main(last_name):
    reddit = praw.Reddit(client_id='HX23RrPh0P0yuw',
                         client_secret='B9CO_uaNQnPuF4DqYQjLWuK0nbQ',
                         user_agent='TheShadowEmperor8055')

    headlines = set()
    try:
        for submission in reddit.subreddit('politics').new(limit=None):
            if last_name.upper() in submission.title.upper():
                headlines.add(submission.title)
    except:
        print()

    sia = SIA()
    results = []

    for line in headlines:
        pol_score = sia.polarity_scores(line)
        pol_score['headline'] = line
        results.append(pol_score)

    with open('../../data/RedditData/headlines.json', 'w') as fp:
        json.dump(results, fp)


# reddit_main(surname)
