from TwitterAPI import TwitterAPI
import twitter

con_secret_key = "ubqVWfkblLhhnkd6glhSxbBJc"
accesstoken = "2989071829-RyJoNTGo8JAGoKLhFh17cY4z2C8wzgz1AKGzhZV"
accestokensecret = "xtnR3c2Vfvk9knUB88PHyiXqcoPzgV4ksJ7xcHdLPbDMx"
con_secret = "m3V96KhISt1FCvLXbyUE6sqU7Arw6Wiu08xaUJTA9s6Qq11RB6"

api = TwitterAPI(con_secret_key,
con_secret,
accesstoken,
accestokensecret)

t = twitter.Twitter(auth=twitter.OAuth(token_secret=accestokensecret, token=accesstoken, consumer_secret=con_secret, consumer_key=con_secret_key))
boo = t.statuses.home_timeline()
for status in boo:
    api.request("statuses/destroy/:{}".format(status['id']))

