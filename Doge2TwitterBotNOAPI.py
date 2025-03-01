import tweepy
import time
import json
from urllib.request import urlopen
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_api_access():
    """
    Authenticate and return the Twitter API object.
    """
    try:
        consumer_key = "YOUR_CONSUMER_KEY"
        consumer_secret = "YOUR_CONSUMER_SECRET"
        access_token = "YOUR_ACCESS_TOKEN"
        access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        api.verify_credentials()  # Verify credentials to ensure authentication is successful
        logging.info("Twitter API authentication successful.")
        return api
    except Exception as e:
        logging.error(f"Failed to authenticate with Twitter API: {e}")
        raise

def get_crypto_information(api_url):
    """
    Fetch cryptocurrency information from the provided API URL.
    """
    try:
        with urlopen(api_url) as response:
            data = json.load(response)
            price_usd = float(data[0]['price_usd'])
            return '${0:.2f}'.format(price_usd)
    except Exception as e:
        logging.error(f"Failed to fetch cryptocurrency information: {e}")
        raise

def post_tweet(api, message):
    """
    Post a tweet with the provided message.
    """
    try:
        api.update_status(status=message)
        logging.info(f"Tweet posted successfully: {message}")
    except Exception as e:
        logging.error(f"Failed to post tweet: {e}")

def main():
    # Replace with your actual API URL
    crypto_api_url = "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin2&vs_currencies=usd"
    
    # Authenticate with Twitter API
    api = get_api_access()
    
    # Main loop to fetch and post cryptocurrency prices
    while True:
        try:
            # Fetch cryptocurrency price
            doge2_price = get_crypto_information(crypto_api_url)
            
            # Compose tweet message
            message = f"Dogecoin2 current price:\n\nDoge: {doge2_price}\n\nThis will update every 4 hours!"
            
            # Post tweet
            post_tweet(api, message)
            
            # Wait for 4 hours before next update
            time.sleep(14400)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            time.sleep(60)  # Wait for 1 minute before retrying

if __name__ == "__main__":
    main()
