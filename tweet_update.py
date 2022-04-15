from bottle import get, view, request, post, redirect
import g 

@post("/update_tweet/<tweet_id>")

def _(tweet_id):
    tweet_id = request.forms.get("tweet_id")
    tweet_title = request.forms.get("tweet_title")
    tweet_description = request.forms.get("tweet_description")
    for tweet in g.TWEETS:
        if tweet["tweet_id"] == tweet_id:
            tweet.update({"tweet_title":tweet_title,"tweet_description":tweet_description}) 
    return redirect("/tweets") 