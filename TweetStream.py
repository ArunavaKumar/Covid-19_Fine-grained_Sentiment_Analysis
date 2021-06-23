import os
import pandas as pd
import tweepy
# import re
# import string
# import preprocessor as p
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

#Twitter credentials for the app
consumer_key = 'bAtnEIPAdwoRbuGmXoX04m3vE'
consumer_secret = 'iq2Z44J26ptHlKjaCBzF0jy54ly8wJQQ3ve0KouvFpjLlST6DK'
access_key = '1240676439755763714-v8GtlVhG6Hm4PZuFadeWSaekcKrvQE'
access_secret = 'PPpdmfFv4Xlti27x1DqntcZ902QZ1AtsrS7IRZrwVvTw6'

#pass twitter credentials to tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#file location changed to "data/telemedicine_data_extraction/" for clearer path
tweets_data = "TweetsDB.csv"

#columns of the csv file
COLS = ['id', 'created_at', 'source', 'original_text', 'lang',
        'favorite_count', 'retweet_count', 'original_author', 'hashtags',
        'user_mentions', 'place']

#method write_tweets()
def write_tweets(keyword, file):
    # If the file exists, then read the existing data from the CSV file.
    if os.path.exists(file):
        df = pd.read_csv('TweetsDB.csv', header=0)
    else:
        df = pd.DataFrame(columns=COLS)
    #page attribute in tweepy.cursor and iteration
    for page in tweepy.Cursor(api.search, q=keyword,
                              count=200, include_rts=False).pages(50):
        for status in page:
            new_entry = []
            status = status._json
            ## check whether the tweet is in english or skip to the next tweet
            if status['lang'] != 'en':
                continue

            #when run the code, below code replaces the retweet amount and
            #no of favorires that are changed since last download.
            if status['created_at'] in df['created_at'].values:
                i = df.loc[df['created_at'] == status['created_at']].index[0]
                if status['favorite_count'] != df.at[i, 'favorite_count'] or \
                   status['retweet_count'] != df.at[i, 'retweet_count']:
                    df.at[i, 'favorite_count'] = status['favorite_count']
                    df.at[i, 'retweet_count'] = status['retweet_count']
                continue
            
            print(status['id'])

			#new entry append
            new_entry += [status['id'], status['created_at'],
                          status['source'], status['text'], status['lang'],
                          status['favorite_count'], status['retweet_count']]

            #to append original author of the tweet
            new_entry.append(status['user']['screen_name'])

            # hashtagas and mentiones are saved using comma separted
            hashtags = ", ".join([hashtag_item['text'] for hashtag_item in status['entities']['hashtags']])
            new_entry.append(hashtags)
            mentions = ", ".join([mention['screen_name'] for mention in status['entities']['user_mentions']])
            new_entry.append(mentions)

            #get location of the tweet if possible
            try:
                location = status['user']['location']
            except TypeError:
                location = ''
            new_entry.append(location)

            single_tweet_df = pd.DataFrame([new_entry], columns=COLS)
            df = df.append(single_tweet_df, ignore_index=True)
            csvFile = open('TweetsDB.csv', 'a', encoding='utf-8')
    df.to_csv('TweetsDB.csv', mode='a', columns=COLS, index=False, encoding="utf-8")

#declare keywords as a query for three categories
tweet_keywords = '#COVID-19 OR #CoronaVirus OR #Covid OR #Covaccine OR #HomeQuarantine OR #LockDown OR #QuarantineCenter OR #SocialDistancing OR #StayHome OR #StaySafe OR #StayAtHomeChallenge'

#call main method passing keywords and file path
write_tweets(tweet_keywords, tweets_data)
