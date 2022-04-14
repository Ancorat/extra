from bottle import get, view, request, post, redirect
import uuid
import g


@post("/create_tweet")

def _():
    tweet_id = str(uuid.uuid4())
    tweet_title = request.forms.get("tweet_title")
    tweet_description = request.forms.get("tweet_description")

    tweet = {"tweet_id":tweet_id,"tweet_title":tweet_title,"tweet_description":tweet_description}
    g.TWEETS.append(tweet)
    return redirect("/tweets")

def delete_function():
    tweet_id = request.forms.get("tweet_id")
    for index, tweet in enumerate(g.TWEETS):
        if tweet["tweet_id"] == tweet_id:
            g.TWEETS.pop(index)
            return redirect("/tweets")