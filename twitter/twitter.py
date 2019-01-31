import config
from requests_oauthlib import OAuth1Session


def get_twitter_session():
    # config.py から読み込む
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET

    return OAuth1Session(CK, CS, AT, ATS)
