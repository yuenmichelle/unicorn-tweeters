import flask
import requests
import json
from requests_oauthlib import OAuth1
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


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

    for tweets in json_object['statuses']:
        result = {
            "username": tweets["user"]["name"],
            "location": tweets["user"]["location"],
            "tweet": tweets["text"],
            "created": tweets["created_at"],
            "retweeted": tweets["retweet_count"],
            "favorited": tweets["favorite_count"]
        }
        filtered_results.append(result)

    return render_template('view.html', results=filtered_results)


@app.route('/retweet', methods=['POST'])
def retweet(tweet_id):
    return render_template('success.html', tweet_id=tweet_id)


@app.route('/favourite', methods=['POST'])
def favourite(tweet_id):
    return render_template('success.html', tweet_id=tweet_id)


app.run()
