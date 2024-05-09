import snscrape.modules.twitter as sntw
import pandas as pd
import json
import snscrape.base
import typing
import datetime
import base

name = str(input("Enter a Twitter username:"))
num = int(input("Enter a number of tweets to scrap:"))

Scraper = sntw.TwitterUserScraper(name, False)

tweets = []

#has no instructions when there are no tweets nor user, pandas dataframe empty
#fails at retrieving the date by adding 'date': tweet.date
#check https://www.youtube.com/watch?v=p8hG8MhzoYc
#original source https://github.com/JustAnotherArchivist/snscrape
#would like to add a nlp column to the pd later
for i, tweet in enumerate(Scraper.get_items()):
    if i > num:
        break
    tweets.append({'id': tweet.id, 'langs': tweet.lang, 'content': tweet.content, 'likes': tweet.likeCount, 'replies': tweet.replyCount, 'retweets': tweet.retweetCount, 'hashtags': tweet.hashtags
    })

#json file
f = open('tweets.json', 'w')
j = json.dumps(tweets)
f.write(j)
f.close()
print(tweets)

#csv file
df = pd.DataFrame.from_dict(tweets)
print(df)