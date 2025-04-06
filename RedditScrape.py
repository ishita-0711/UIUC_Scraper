import praw

with open('secrets.txt', 'r') as file:
    bot_id, secret_key = file.read().split(',')
#

reddit = praw.Reddit(
    client_id=bot_id,
    client_secret=secret_key,
    user_agent="UIUCScrape",
)
for submission in reddit.subreddit("UIUC").hot(limit=10):
    print(submission.title)