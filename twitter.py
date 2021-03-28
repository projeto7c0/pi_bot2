import tweepy
import twitter_auth

def tweet(status_text):
    api = twitter_auth.authenticate()
    status = api.update_status(status=status_text)
           
    return status
