# Reddit-Bot1

Hey, This is my First Reddit Bot to get new topics from subreddit


## Requirements-  
* Python3

Python libraries used-  
* praw(for reddit)  
* notify(for notification in ubuntu)**Works only in ubuntu as far as i know**  

## Installing python libraries

* installing praw-  
`pip3 install praw`  

* installing notify  
`pip3 install notify2`  

## Todo after getting all files

* Login into Reddit  
* Register for app  
* give it some name  
* now you'll get client id and secret. Keep it safe  
* pull this repo
* open config.py

### Here you fill following info-
* username-You Reddit username  
* password-Your Reddit Password  
* clientid- id you got from creating app in reddit  
* client_secret - secret key you get when creating app in reddit  
* user_agent - Well give it any name(eg 'MyBot v0.1'). This is now needed for oauth in reddit  

Finally run-  
`python3 redbot.py`
