# Unicorn Tweeters Challenge

1) Add Tweet ID to be displayed
(Hint:
```"id":1049783444971147271```, files to be changed ```view.html``` and ```run.py```)
2) Add Times Retweeted to be displayed (```view.html``` and ```run.py```) (Hint: ```"retweet_count": 2```)
3) Add Times Favourited to be displayed (```view.html``` and ```run.py```) (Hint: ```"favorite_count": 1```)
4) Add new 'Retweet' functionality to the website (```view.html```)
5) Implement 'Retweet' functionality in Python (```run.py```)
6) Add new 'Tweet' functionality to the website (```view.html```)
7) Implement 'Tweet' functionality in Python (```run.py```)
8) Customise your website, change it to your favourite colours, change 'Unicorn Tweeters' to your unique team name
9) Draw some other functionality you'd love to see and think about how

## Commands to get you started

Make sure you are in the right directory:

```
pwd
```

If you are then it will return with ```/pi/home/Desktop/unicorn-tweeters```

If you are not, then call ```cd Desktop/unicorn-tweeters``` (depending where you are)

To run the Python script, simply call:

```
python3 run.py
```

The front-end webpage is accessible by typing the following into your Browser:

```
http://127.0.0.1:5000
```

## Endpoints of interest

#### Favourite

```
https://api.twitter.com/1.1/favorites/create.json?id={tweet_id}
```
e.g.
```
https://api.twitter.com/1.1/favorites/create.json?id=1050063156230410240
```

#### Retweet

```
https://api.twitter.com/1.1/statuses/retweet/{tweet_id}.json
```
e.g.
```
https://api.twitter.com/1.1/statuses/retweet/1050063156230410240.json
```

#### Post new tweet

```
https://api.twitter.com/1.1/statuses/update.json
```

Body: key ```status```, value {{status}}


### Solution Hints

```
tweets["id"]
```

```
tweets["favorite_count"]
```

```
requests.post(url="https://api.twitter.com/1.1/statuses/retweet/" + tweet_id + ".json", auth=oauth)
```

```
payload = { 'status' : 'Hi everyone at #bpsfleet' }
requests.post(url="https://api.twitter.com/1.1/statuses/update.json", data=payload, auth=oauth)
```

```
parameters = { "id": tweet_id }
response = requests.post(url="https://api.twitter.com/1.1/favorites/create.json", auth=get_oauth(), params=parameters)
```
