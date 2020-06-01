import re  # regular expression kütüphanesi. python ile standart olarak gelir, kurulum gerektirmez.
import tweepy  # Twitter API'sına erişmek için bir Python kütüphanesi.
from tweepy import OAuthHandler  # Twitter API'sını bağlamak için.
from textblob import TextBlob
import sys


class TwitterClient(object):
	# Şüphesiz Tweepy kullanarak Twitter’a erişmek için öncelikle bir Twitter API erişimi kullanıyoruz.
	
	def __init__(self):
		consumer_key = ''
		consumer_secret = ''
		access_token = ''
		access_token_secret = ''
		# API erişimimiz sonucu artık bize verilen özel anahtarlar; Consumer Key, Consumer Secret, Access Token ve Access Token Secret değerleridir. Bu anahtarları kullanarak, Tweepy methodlarına erişebiliriz.
		try:
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			self.auth.set_access_token(access_token, access_token_secret)
			self.api = tweepy.API(self.auth)
		except:
			print("Hata: Authentication doğrulaması yanlış!")
	
	# Bağlantımız sağlandı. Bu noktadan sonra Tweepy metodlarını kullanarak Tweetler üzerinde çeşitli işlemler yapabiliriz. Tweetlerle ilgili metodlarda bir Tweet JSON dönecektir (Status nesnesi).
	# Fetchlediğimiz twitleri regex ifadesi kullanarak, istemediğimiz karakterlerden arındırıyoruz.
	def clean_tweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0–9_]+)|(#+)|(RT[\s]+)|(https?:\/\/\S+)", " ", tweet).split())
	
	def get_tweet_sentiment(self, tweet):
		# Dışarıdan ulaşılmasını istediğimiz her fonksiyona self parametresini eklememiz gerekmektedir.
		# Konuşma bölümü etiketleme, isim öbeği çıkarma, duygu analizi, sınıflandırma, çeviri ve daha fazlası gibi ortak doğal dil işleme (NLP) görevlerine dalmak için bir API sağlar.
		# Burada TextBlob methoduna bir text nesnesi veririz, TextBlob bizi uğraştırmadan bu nesneyi bir dil işlemeden geçirir. Yani kelime köklerini bölmek, yanlış yazılmış kelimeleri düzeltmek vs.
		# Bununla kalmaz, kendi datasetindeki kelimelere göre bir duygu polarite ölçümü de sağlar bizim için.
		analysis = TextBlob(self.clean_tweet(tweet))
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'
	
	# twitten metinler alınır.
	def get_tweets(self, query, count=1000):
		tweets = []
		# parse edilmiş tweet'leri saklamak için boş liste
		
		try:
			# q değişkeni altındaki twit sayısını al..
			# tweetleri almak için twitter api çağırılır.
			fetched_tweets = self.api.search(q=query, count=count)
			# tweetleri tek tek parse ediyoruz.
			for tweet in fetched_tweets:
				# her tweetin bir metnini diziye ekle.
				parsed_tweet = {}
				non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1),
				                            0xfffd)  # ingilizceye ait olmayan encode ifadeleri almak için.
				# tweet metnini almak.
				parsed_tweet['text'] = tweet.text.translate(non_bmp_map)
				# tweete ait duygu analazinin polaritesini almak.
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
				if tweet.retweet_count > 0:
					
					# buradaki koşul aracalığıyla parse ettiğimiz tweeti, tweets listelesine ekleyeceğiz.
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
				else:
					tweets.append(parsed_tweet)
			
			return tweets
		
		except tweepy.TweepError as e:
			# print error (if any)
			print("Hata : " + str(e))


class TwitterObject(object):
	def __init__(self):
		# TwitterClient Sınıfı nesnesi oluşturma.
		self.api = TwitterClient()
		self.subj = ''
		self.ptweets = []
		self.tweets = []
		self.ntweets = []
		self.neutral = []
	
	def fetchTweets(self):
		self.tweets = self.api.get_tweets(self.subj, count=1000)
		self.ptweets = [tweet for tweet in self.tweets if tweet['sentiment'] == 'positive']
		self.ntweets = [tweet for tweet in self.tweets if tweet['sentiment'] == 'negative']
		self.neutral = [tweet for tweet in self.tweets if tweet['sentiment'] == 'neutral']
