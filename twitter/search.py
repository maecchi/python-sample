# coding: UTF-8
import json
import twitter as tweets

twitter = tweets.get_twitter_session()

url = "https://api.twitter.com/1.1/search/tweets.json"

print("何を調べますか?")
keyword = input('>> ')
print('----------------------------------------')

params = {'q': keyword, 'count': 5}

request = twitter.get(url, params=params)

if request.status_code == 200:
    search_timeline = json.loads(request.text)
    for tweet in search_timeline['statuses']:
        print(tweet['user']['name'] + '::' + tweet['text'])
        print(tweet['created_at'])
        print('----------------------------------------')
else:
    print("ERROR: %d" % request.status_code)
