import praw
import config
import time
import notify

topic_unseen = []

#used to login in reddit, (needed for running Reddit Api)
def bot_login():
	r=praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = config.user_agent)
	return r

def run_bot(r):
	#This is how you define which Subreddit to get topics from.
	# You can have multiple subreddits defined
	subred = r.subreddit("learnpython")

	# getting latest topics in subreddit , limit=no of topics to get at a time
	for submission in subred.new(limit=5):
		# Checking if we've a;ready seen this topic
		if submission.title not in topic_unseen:
			print("Title: ", submission.title)
			print("URl: ", submission.url)
			print("---------------------------------")
			topic_unseen.append(submission.title)

			#This is for getting notification in ubuntu
			# When running on other systemm remove this line
			notify.put_top(submission.title,submission.url)

			#I don't want to get bombarded with all topics at once so kept a timer
			time.sleep(2)
	# Time to recheck the time for new topics
	time.sleep(10)

#calling Login only once, since we need to login only once
r = bot_login()
#This will run forever checking new Topics in Reddit
while True:
	run_bot(r)
