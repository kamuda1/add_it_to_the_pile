import praw
from config import client_id, client_secret
import requests

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='useragent',
                     )

def get_atrocities():
    "reads attrocities from the url into a list"
    atrocities_url = 'https://www.mcsweeneys.net/articles/the-complete-listing-so-far-atrocities-1-944'
    page = requests.get(atrocities_url)
    page.text.split('&#8211')[18]


if __name__ == '__main__':
    submissions = reddit.subreddit("Politics").hot(limit=1000)
    for submission in submissions:
        for comment in submission.comments:
            post_string = comment.body
            if 'throw' in post_string or 'pile' in post_string:
                pass
