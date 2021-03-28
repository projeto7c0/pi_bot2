import tweepy


def autentica_list():
    api_key = ''
    api_secret_key = ''
    access_token = ''
    access_token_secret = ''

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60,
                     retry_errors=set([503]))

    return api
