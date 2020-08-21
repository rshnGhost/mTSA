import argparse
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from main.password import fetch

class TwitterClient(object):
	'''
	Generic Twitter Class for sentiment analysis.
	'''
	def __init__(self):
		'''
		Class constructor or initialization method.
		'''
		# keys and tokens from the Twitter Dev Console
		consumer_key = fetch('consumer_key')
		consumer_secret = fetch('consumer_secret')
		access_token = fetch('access_token')
		access_token_secret = fetch('access_token_secret')

		#print(consumer_key)
		#print(consumer_secret)
		#print(access_token)
		#print(access_token_secret)
		# attempt authentication
		try:
			# create OAuthHandler object
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			# set access token and secret
			self.auth.set_access_token(access_token, access_token_secret)
			# create tweepy API object to fetch tweets
			self.api = tweepy.API(self.auth)
		except:
			print("Error: Authentication Failed")

	def clean_tweet(self, tweet):
		'''
		Utility function to clean tweet text by removing links, special characters
		using simple regex statements.
		'''
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	def get_tweet_sentiment(self, tweet):
		'''
		Utility function to classify sentiment of passed tweet
		using textblob's sentiment method
		'''
		# create TextBlob object of passed tweet text
		analysis = TextBlob(self.clean_tweet(tweet))
		# set sentiment
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'

	def get_tweets(self, query, count = 10):
		'''
		Main function to fetch tweets and parse them.
		'''
		# empty list to store parsed tweets
		tweets = []

		try:
			# call twitter api to fetch tweets
			#print(query)
			fetched_tweets = self.api.search(q = query, lang = "en", count = count)

			# parsing tweets one by one
			for tweet in fetched_tweets:
				# empty dictionary to store required params of a tweet
				parsed_tweet = {}

				# saving text of tweet
				parsed_tweet['text'] = tweet.text
				# saving sentiment of tweet
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

				# appending parsed tweet to tweets list
				if tweet.retweet_count > 0:
					# if tweet has retweets, ensure that it is appended only once
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)
			# return parsed tweets
			return tweets

		except tweepy.TweepError as e:
			# print error (if any)
			print("Error : " + str(e))

class Twitter:
	def __init__(self , tag):
		api = TwitterClient()
		tweets = api.get_tweets(query = tag ,count = 200)
		total = self.tt = len(tweets)
		# percentage of positive tweets
		ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
		self.ptweetst = str(ptweets)
		self.pt = len(ptweets)
		# percentage of negative tweets
		ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
		self.ntweetst = str(ntweets)
		self.nt = len(ntweets)
		# for neutral tweets
		nntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
		self.nntweetst = str(nntweets)
		self.nnt = len(nntweets)
		if len(tweets):
			self.net = len(tweets)-(len(ptweets)+len(ntweets))
		else:
			self.net = 0
		self.name = str(tag)
		#self.ntweets[:10]
		#print(self.name,self.pt,self.nt,self.net,self.tt,total)
		#print(len(ptweets),len(ntweets),len(tweets),len(tweets))

def process(name):
	return Twitter(name)
