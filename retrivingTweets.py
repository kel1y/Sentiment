!pip install git+https://github.com/tweepy/tweepy.git


import os
import tweepy
import pandas as pd

# Load Twitter API credentials from Kaggle Secrets
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_SECRET')

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

api = tweepy.API(auth, wait_on_rate_limit=True)


# Query: about distance-based fare in Rwanda
search_query = (
    '(fare OR fares OR "distance-based fare" OR "fare system" OR transport OR bus OR taxi OR RURA OR "public transport") '
    'AND (Rwanda OR Kigali) '
    '-filter:retweets -filter:replies -filter:links'
)


no_of_tweets = 100

try:
    tweets = api.search_tweets(q=search_query, lang="en", count=no_of_tweets, tweet_mode='extended')

    # Extract selected attributes
    attributes_container = [
        [tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text]
        for tweet in tweets
    ]

    # Define DataFrame structure
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    tweets_df = pd.DataFrame(attributes_container, columns=columns)

    # Preview
    tweets_df.head()
except Exception as e:
    print("Status Failed:", str(e))


# Save tweets to CSV for later analysis
tweets_df.to_csv("rwanda_transport_tweets.csv", index=False)


