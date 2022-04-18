from bottle import get, view, request, redirect
import g

@get("/tweets")
@view("tweet")
def _():
    error = request.params.get("error")
    tweet_title = request.forms.get("tweet_title")
    tweet_description = request.forms.get("tweet_description")

    return dict(tweets = g.TWEETS, tweet_title = tweet_title, tweet_description = tweet_description, error=error)