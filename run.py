from datetime import datetime
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

    for tweets in json_object['statuses']:
        result = []
        result.append(tweets["user"]["name"])
        result.append(tweets["user"]["location"])
        result.append(tweets["text"])
        result.append(datetime.strptime(tweets["created_at"], '%a %b %d %H:%M:%S %z %Y').strftime('%d/%m/%Y %H:%M:%S'))

        filtered_results.append(result)

    return render_template('view.html', results=filtered_results)


@app.route('/retweet', methods=['POST'])
def retweet():
    tweet_id = request.form['tweet_id']
    response = requests.post(url="https://api.twitter.com/1.1/statuses/retweet/" + tweet_id + ".json", auth=get_oauth())
    if response.ok:
        return render_template('success.html', outcome="Action completed for Tweet ID " + tweet_id)
    else:
        return render_template('failure.html')


app.run()
