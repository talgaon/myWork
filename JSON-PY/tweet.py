 #
 # import json
 # f = open("twitter_small.json", "r")
 # tweets = json.load(f)
 # f.close()
 # for tweet in tweets:
 #      text = tweet["text"]
 #       print(text)
'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("twitter_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
