import flask
import requests
import json
from requests_oauthlib import OAuth1
from flask import render_template, request

app = flask.Flask(__name__)


REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"


def get_oauth():
    with open("credentials.json") as f:
        data = json.load(f)

    oauth = OAuth1(data["CONSUMER_KEY"],
                   client_secret = data["CONSUMER_SECRET"],
                   resource_owner_key = data["OAUTH_TOKEN"],
                   resource_owner_secret = data["OAUTH_TOKEN_SECRET"])
    return oauth


@app.route('/', methods=['GET'])
def home():
    oauth = get_oauth()
    response = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=bpsfleet", auth=oauth)

    filtered_results = []
    json_object = json.loads(response.text)
    print(json_object)

    for tweets in json_object['statuses']:
        result = []
        result.append(tweets["user"]["name"])
        result.append(tweets["user"]["location"])
        result.append(tweets["text"])
        result.append(tweets["created_at"])
        result.append(tweets["retweet_count"])
        result.append(tweets["favorite_count"])
        result.append(tweets["id"])

        filtered_results.append(result)

    return render_template('view.html', results=filtered_results)


@app.route('/retweet', methods=['POST'])
def retweet():
    tweet_id = request.form['tweet_id']
    response = requests.post(url="https://api.twitter.com/1.1/statuses/retweet/" + tweet_id + ".json", auth=get_oauth())
    if response.ok:
        return render_template('success.html', tweet_id=tweet_id)
    else:
        return render_template('failure.html', tweet_id=tweet_id)


@app.route('/favourite', methods=['POST'])
def favourite():
    tweet_id = request.form['tweet_id']
    parameters = { "id": tweet_id }
    response = requests.post(url="https://api.twitter.com/1.1/favorites/create.json", auth=get_oauth(), params=parameters)
    if response.ok:
        return render_template('success.html', tweet_id=tweet_id)
    else:
        return render_template('failure.html', tweet_id=tweet_id)


app.run()
