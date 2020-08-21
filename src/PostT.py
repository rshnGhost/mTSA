import tweepy
from tweepy import OAuthHandler
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

	def tweetCoustom(self, status):
		try:
			# call twitter api to post tweets
			#fetched_tweets = self.api.search(q = query, count = count)
			status = self.api.update_status(status=status)
			return status._json.get('id')
		except tweepy.TweepError as e:
			# print error (if any)
			print(eval(str(e))[0].get('message'))#
			return (eval(str(e))[0].get('message'))

class Tweet:
	def __init__(self , tweet):
		api = TwitterClient()
		self.status = api.tweetCoustom(status=tweet)
		#print(self.status)

def PostT(name):
	return Tweet(name)
