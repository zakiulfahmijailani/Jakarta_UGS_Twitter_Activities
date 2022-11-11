# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:53:20 2022

@author: zakiu
"""

import tweepy
#from twitter_authentication import bearer_token
import time
import pandas as pd
import sys

API_KEY = "vRec4q8kEV06xpORLGahNYenh"
API_KEY_SECRET = "NshLsA0MCzuKicMMhNOI4PMwONvkEWjbP6N3FXTPk68QaL19Dd"
ACCESS_TOKEN = "1590540102219886592-rfQsoeuQHbTUFmO9on3e6q55wNyqSr"
ACCESS_TOKEN_SECRET = "RW7Z8vEfKrWIEuwC88WRWak2ZcJroyyHst9sPSGeTK2bI"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAM6jjAEAAAAA9wJtldNSTN%2BxNIXVgvpWtcngu%2F4%3D7tjFyowKx7VOzFv9m3oauJZGluPbqzmTp8oLYpVvsMBcSuh72f"

Client_ID = "WnRrLVBOeHJRMlp2QTQwdTBpTFo6MTpjaQ"
Client_Secret = "4Z5VP6sLdiXhlb0iPZ20YKQArN2f8fEdrLNkawY1q2vCZBW5iB"

consumer_key = API_KEY
consumer_secret = API_KEY_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

bearer_token = BEARER_TOKEN

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet_lst=[]
geoc="38.9072,-77.0369, 13mi"
search_words = ""

for tweet in tweepy.Cursor(api.search_tweets,q=search_words, geocode=geoc).items(1000):
    tweetDate = tweet.created_at.date()
    if(tweet.coordinates !=None):
        tweet_lst.append([tweetDate,tweet.id,tweet.
                coordinates['coordinates'][0],
                tweet.coordinates['coordinates'][1],
                tweet.user.screen_name,
                tweet.user.name, tweet.text,
                tweet.user._json['geo_enabled']])
tweet_df = pd.DataFrame(tweet_lst, columns=['tweet_dt', 'id', 'lat','long','username', 'name', 'tweet','geo'])



# =============================================================================
# public_tweets = api.home_timeline()
# print(public_tweets)
# =============================================================================
# =============================================================================
# 
# search_words = "jakarta"
# date_since = "2021-01-01"
# 
# tweets = tweepy.Cursor(api.search_tweets,
#               q = search_words,
#               lang = "en",
#               since = date_since).items(5)
# 
# def get_related_tweets(key_word):
#     twitter_users = []
#     tweet_time = []
#     tweet_string = [] 
#     for tweet in tweepy.Cursor(api.search_tweets,q=key_word, count=1000).items(1000):
#             if (not tweet.retweeted) and ('RT @' not in tweet.text):
#                 if tweet.lang == "en":
#                     twitter_users.append(tweet.user.name)
#                     tweet_time.append(tweet.created_at)
#                     tweet_string.append(tweet.text)
#                     
#     df = pd.DataFrame({'name':twitter_users, 'time': tweet_time, 'tweet': tweet_string})
#     df.to_csv(f"{key_word}.csv")
#     return df
# 
# df = get_related_tweets("jakarta")
# df.head(7)
# =============================================================================

# =============================================================================
# # web crawling now
# client = tweepy.Client(bearer_token, wait_on_rate_limit=True)
# 
# hoax_tweets = []
# for response in tweepy.Paginator(api.search_all_tweets, 
#                                   query = "from:Twitterdev -is:retweet has:geo",
#                                   user_fields = ['username', 'public_metrics', 'description', 'location'],
#                                   tweet_fields = ['created_at', 'geo', 'public_metrics', 'text'],
#                                   expansions = 'author_id',
#                                   start_time = '2019-01-01T00:00:00Z',
#                                   end_time = '2020-01-01T00:00:00Z',
#                               max_results=500):
#     time.sleep(1)
#     hoax_tweets.append(response)
# 
# =============================================================================
