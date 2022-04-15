from bottle import run, get, post, delete 
import signup_get
import signup_post
import g
import login_get
import index_get
import login_post
import tweet_get
import tweet_post
import tweet_delete
import tweet_update

run(host="127.0.0.1", port=8888, debug=True, reloader=True)

