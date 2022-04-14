from bottle import get, view, request
import g

@get("/tweets")
@view("tweet")

def _():
    tweet_title = request.forms.get("tweet_title")
    tweet_description = request.forms.get("tweet_description")
    return dict(tweets = g.TWEETS, tweet_title = tweet_title, tweet_description = tweet_description)