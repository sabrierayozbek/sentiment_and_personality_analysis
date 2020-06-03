[![GitHub issues](https://img.shields.io/github/issues/sabrierayozbek/sentiment_and_personality_analysis.svg)](https://github.com/sentiment_and_personality_analysis/issues)
[![GitHub forks](https://img.shields.io/github/forks/sabrierayozbek/sentiment_and_personality_analysis.svg)](https://github.com/sentiment_and_personality_analysis/network)


# Sentiment And Personality Analysis For Twitter Users
 This software presents you to do sentiment and personality analysis for twitter users.

## Introduction: 

As part of the study, a web-based software was developed using the Python programming language and the Django software framework.

![sentiment_and_personality_analysis main](https://github.com/sabrierayozbek/sentiment_and_personality_analysis/blob/master/images/main.png)

When you the as a user accesses interface, you can choose one of the sentiment and personality analysis.

**Block diagram of the use of the application:**
![sentiment_and_personality_analysis schema](https://github.com/sabrierayozbek/sentiment_and_personality_analysis/blob/master/images/schema.png)

**An example personality analysis:**
![sentiment_and_personality_analysis personality](https://github.com/sabrierayozbek/sentiment_and_personality_analysis/blob/master/images/personality.png)

**An example sentiment analysis:**
![sentiment_and_personality_analysis sentiment](https://github.com/sabrierayozbek/sentiment_and_personality_analysis/blob/master/images/sentiment.png)


## Requirements: 
- Python 3+
- Django
- Python ReGex
- Tweepy
- TextBlob
- GingerIt 


## Usage: 


```
	 consumer_key = ''
		consumer_secret = ''
		access_token = ''
		access_token_secret = ''

```

Firstly, we should use a Twitter API access to access Twitter using Tweepy. Private keys given to us as a result of our API access; Consumer Key, Consumer Secret, Access Token and Access Token Secret are values. Using these keys, we can access the Tweepy methods. 
You can get these keys from twitter developer site. (https://developer.twitter.com)

**After this step, you can write this command on the console screen and run it.**

```
python manage.py runserver
```
