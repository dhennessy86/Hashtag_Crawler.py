from secret import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy as ty
import csv
import re

"""
Script Created on : 25th Oct 2017
Script Purpose:
	This script will search twitter for Scanner URL links from tweets containing a certain hashtag
	The output of each positive hit goes to a CSV
"""
#Regex 
Regex = ".*hybrid-analysis.com\/.*|.*virustotal.com\/.*|.*malwr.com\/.*"

#Authorizes the code
auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = ty.API(auth)

# Tweet hashtags to check for
hashtag = "#badrabbit"

#Retrieve the tweets for hashtag
hashtag_tweets = []

#Create CSV for Scanner Links
f = open('%s_Links.csv' % hashtag , 'wb')
writer = csv.writer(f)
writer.writerow(["CSV for VT & Hybrid Links"])
f.close()

# Tweet search -> https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
# Default no. of tweets is 15

for tweet in ty.Cursor(api.search, q=hashtag, result_type="mixed" , include_entities = 'True').items(20):
	hashtag_tweets.extend([tweet.text])
	User = tweet.user.name
	if not tweet.entities['urls']:										#check if tweet has any URL's if its blank skip tweet
		pass
	else:
		URL =  tweet.entities['urls'][0]['expanded_url']
		#print URL
		check = re.findall(Regex , URL , re.IGNORECASE) 
		if check:
			print URL
			# Output URL to CSV
			f = open('%s_Links.csv' % hashtag , 'a+')
			writer = csv.writer(f)
			writer.writerow([URL])
		else:
			print "Tweet did not contain required links"

