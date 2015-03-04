#from twitter import *
#from twitter import Twitter, OAuth
import twitter
import time


def sendTwitterUpdateStatus(message):
    con_secret_key = "ubqVWfkblLhhnkd6glhSxbBJc"
    accesstoken = "2989071829-RyJoNTGo8JAGoKLhFh17cY4z2C8wzgz1AKGzhZV"
    accestokensecret = "xtnR3c2Vfvk9knUB88PHyiXqcoPzgV4ksJ7xcHdLPbDMx"
    con_secret = "m3V96KhISt1FCvLXbyUE6sqU7Arw6Wiu08xaUJTA9s6Qq11RB6"
    t = twitter.Twitter(auth=twitter.OAuth(token_secret=accestokensecret, token=accesstoken, consumer_secret=con_secret, consumer_key=con_secret_key))
    t.statuses.update(status=message)
    print('Tweet sent.')


timesent = time.strftime("%a %d %b %Y %H:%M:%S", time.localtime())
tweet = 'Tweet sent from file sendtweet.py on ' + timesent
sendTwitterUpdateStatus(tweet)
someJunkText = "dasdasdadsdfsdsfsdfs";




















'''
if __name__ == "__main__":
	#pass
    #sendTwitterUpdateStatus('Tweet sent from file sendtweet.py')
'''
'''
else:
    print(__name__)
'''