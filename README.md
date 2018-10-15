# Unicorn Tweeters

This is a Python challenge designed to allow you to call the [Twitter API](https://developer.twitter.com/en/docs).


# The Challenge

1) Add Tweet ID to be displayed
(Hint:
```id":1049783444971147271```, files to be changed ```view.html``` and ```run.py```)
2) Replace the retweet API calls to make real calls to the Twitter API. App route ```@retweet```.
3) Replace the favourite API calls to make real calls to the Twitter API. App route ```@favourite```.
4) Bonus: If you have aced the above, add a new html form to ```view.html``` which calls a new app route called ```tweet```.

## What is provided
* A webpage where you can find all tweets containing #bpsfleet
* Python code which shows how to call the search tweets endpoint


## Commands to get you started

Make sure you are in the right directory:

```
pwd
```

If you are then it will return with ```/Users/michelleyuen/unicorn-tweeters```

If you are not, then call ```cd unicorn-tweeters``` (depending where you are)

To run the Python script, simply call:

```
python3 run.py
```

The front-end webpage is accessible by typing the following into your Browser:

```
http://127.0.0.1:5000
```

## Endpoints of interest

Retweet

```
https://api.twitter.com/1.1/statuses/retweet/{tweet_id}.json
```
e.g.
```
https://api.twitter.com/1.1/statuses/retweet/1050063156230410240.json
```

Favourite

```
https://api.twitter.com/1.1/favorites/create.json?id={tweet_id}
```
e.g.
```
https://api.twitter.com/1.1/favorites/create.json?id=1050063156230410240
```

Post new tweet

```
https://api.twitter.com/1.1/statuses/update.json
```

Body: key ```status```, value {{status}}


## Code snippets
To print something out into the terminal:
```
print({variable})
```
e.g.
```
print(response.text)
```


### Solution Hints

```
tweets["id"]
```

```
requests.post(url="https://api.twitter.com/1.1/statuses/retweet/" + tweet_id + ".json", auth=oauth)
```

```
payload = { 'status' : 'Hi everyone at #bpsfleet' }
requests.post(url="https://api.twitter.com/1.1/statuses/update.json", data=payload, auth=oauth)
```
