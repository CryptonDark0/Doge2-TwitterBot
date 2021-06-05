import tweepy
import time
import json
from urllib.request import urlopen

def get_api_access():
	"""
		NOTE:
		The consumer key and access token can be found by going to app.twitter.com
		
	"""
	consumer_key = ""
	consumer_secret = ""

	access_token = ""
	access_token_secret = ""

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)

def get_crypto_information():

	doge2_api = urlopen("")#!Insert api to doge2
	doge2_data = json.load(doge2_api)


	doge2_price = '${0:.2f}'.format(float(doge2_data[0]['price_usd']))
	return doge2_price

api = get_api_access()
while True:
	doge2_price()
	message = "Dogecoin 2.0 current prices:\n\nDoge2: " + doge2_price +"\n\nThis will update every (null)!"
	
	api.update_status(status=message)
	time.sleep(14400) #!Insert variable by seconds.
