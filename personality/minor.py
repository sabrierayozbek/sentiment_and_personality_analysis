import tweepy #https://github.com/tweepy/tweepy
import csv
import re
#import thread 
import threading #Python'da paralel işlem yapmak için kullanılır.
# Standart Python kütüphanesindeki threading, multiprocessing, subprocess gibi üst-seviye modüller bu kütüphane aracılığıyla kolay bir şekilde yapılabiliyor.
import datetime #Formatlı tarih ve saat kullanımı.
import time
from gingerit.gingerit import GingerIt #Her cümleyi web'den milyarlarca benzer cümle ile karşılaştırarak tam cümleler bağlamına göre yazım ve dilbilgisi hatalarını düzelten bir dil işleme kütüphanesi.
#Daha fazla bilgi için bu dökümantasyona bakabilirsiniz.

#https://gingerit.readthedocs.io/en/latest/
from tweepy import OAuthHandler
from textblob import TextBlob
import sys

#Şüphesiz Tweepy kullanarak Twitter’a erişmek için öncelikle bir Twitter API erişimi kullanıyoruz.
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


parser = GingerIt() #Grammer doğrulama sağlıyoruz.
"""
 "text" => "The smelt of fliwers bring back memories.",
 "result" => "The smell of flowers brings back memories.",
"""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Bağlantımız sağlandı. Bu noktadan sonra Tweepy metodlarını kullanarak Tweetler üzerinde çeşitli işlemler yapabiliriz. Tweetlerle ilgili metodlarda bir Tweet JSON dönecektir (Status nesnesi).


tweets=[]
agreecount=0
opticount=0
negtweet=0
critcount=0
pessicount=0
postweet=0
viewholdercount=0
neuttweet=0
neucount=0
viewtweet=0
grammar=0
aciklik=0
sorumluluk=0
disa_donukluk=0
uyumluluk=0
duygusal_denge=0

non_bmp_map=dict.fromkeys(range(0x10000, sys.maxunicode+1), 0xfffd) #ingilizceye ait olmayan encode ifadeleri almak için.

parser = GingerIt() #Grammer doğrulama sağlıyoruz.

class myThread(threading.Thread):


    #Thread sınıfı, ayrı bir denetim iş parçacığında çalışan bir etkinliği temsil eder.
    # Etkinliği belirtmenin iki yolu vardır: oluşturucuya çağrılabilir bir nesne ileterek. alt sınıftaki run () yöntemini geçersiz kılarak.
                def __init__(self,counter,tweet,hashtag): #_init__, Python'da rezerve edilmiş yöntemlerden biridir. Nesneye yönelik programlamada, yapıcı olarak bilinir.
                    # _init__ yöntemi, sınıftan bir nesne oluşturulduğunda çağrılabilir ve sınıfın niteliklerini başlatmak için erişim gerekir.
                                threading.Thread.__init__(self) # Python'da kendi iş parçacığımızı oluşturmak için sınıfımızın iş parçacığı olarak çalışmasını istiyoruz.
                                                                # Bunun için, sınıfımızı Thread sınıfından alt sınıflara ayırmalıyız.
                                self.counter=counter
                                self.tweet=tweet
                                self.hashtag=hashtag
        
                """
                Bir İş Parçacığı başlatıldığında, bazı temel başlatmalar yapar ve ardından yapıcıya iletilen hedef işlevi çağıran run () yöntemini çağırır.
                Thread sınıfı, ayrı bir denetim iş parçacığında çalışan bir etkinliği temsil eder. Etkinliği belirtmenin iki yolu vardır:
                1) oluşturucuya çağrılabilir bir nesne ileterek
                2) bir alt sınıfta run () yöntemini geçersiz kılarak

                Alt sınıfta başka hiçbir yöntem (kurucu hariç) geçersiz kılınmamalıdır. Başka bir deyişle, yalnızca bir sınıfın __init __ () ve run () yöntemlerini geçersiz kılar.
                
                Biz bu projede, iş parçacığının bir alt sınıfını oluşturacağız ve ne gerekiyorsa yapmak için run () öğesini geçersiz kılacağız:
                """
                          
                def run(self):
                    #run methodu çağırılır.

                                

                                parsed_tweet={}   # her tweetin bir metnini diziye eklemek için.
                                parsed_tweet['text']=self.tweet.translate(non_bmp_map) #tweetleri unicode karakterlerle birlikte al.
                                parsed_tweet['sentiment'] = self.get_tweet_sentiment(str(self.tweet))
                                #tweete ait duygu analazinin polaritesini almak.
                                tweets.append(parsed_tweet) #parse ettiğimiz tweetleri tweets listesine ekliyoruz.
                                ptweets= self.get_tweets(self.hashtag,30) #eğer,kullanıcının hashtag kullanarak attığı bir tweet varsa bunu
                                #analizimizde kullanabiliriz.

                                if(tweets):
                                     global agreecount,opticount,negtweet,critcount,pessicount,postweet,viewholdercount,neuttweet,neucount,viewtweet,grammar,aciklik,sorumluluk,disa_donukluk,uyumluluk,duygusal_denge

                                if ptweets=="0" or ptweets==0: #Eğer çekilen tweetlerde hashtag yoksa, direkt hashtag'siz tweetin duygu polaritesi atılır.
                                                ptweets=parsed_tweet['sentiment']
                                if ptweets==parsed_tweet['sentiment']: #eğer hashtag polaritesi ile tweetin polaritesi aynı ise uygunluk sayısını arttırıyoruz.
                                                
                                                agreecount+=1
                                                uyumluluk+=1
                                                aciklik-=1
                                                sorumluluk+=1
                                                duygusal_denge+=1
                                               
                                                
                                if str(ptweets)=='positive' and parsed_tweet['sentiment']=='negative':
                                    #eğer bir hashtag negatif ve tweet'imiz de negatifse kötümserlik sayısı artacaktır. #eğer bir hashtag pozitif ve tweet'imiz de negatifse kötümserlik sayısı artacaktır.
                                                
                                                pessicount += 1
                                                aciklik+=1
                                                duygusal_denge-=1
                                                uyumluluk-=1
                                                disa_donukluk-=1
                                               
                                                #print("2 ->", pessicount)
                                if str(ptweets) == 'negative' and parsed_tweet['sentiment'] == 'positive':
                                                
                                                opticount+=1
                                                critcount+=1
                                                aciklik+=1
                                                uyumluluk+=1
                                                duygusal_denge+=1
                                                disa_donukluk+=1
                                                
                              
                                if str(ptweets)=='neutral':
                                                
                                                neuttweet+=1
                                                aciklik-=1
                                                uyumluluk+=1
                                                duygusal_denge+=1
                                                disa_donukluk-=1
                                                sorumluluk+=1
                                                
                                               #print("6 ->", neuttweet)
                                if str(ptweets)!='neutral' and parsed_tweet['sentiment']=='neutral':
                                                
                                                viewholdercount+=1
                                                aciklik-=1
                                                disa_donukluk-=1
                                                uyumluluk-=1
                                                duygusal_denge-=1
                                               
                                if str(ptweets)!='neutral':
                                                
                                                viewtweet+=1
                                                aciklik+=1
                                                disa_donukluk+=1
                                                duygusal_denge-=1
                                                
                                                #print("7 ->", viewtweet)
                                if str(ptweets)=='neutral' and parsed_tweet['sentiment']=='neutral':
                                                
                                                neucount+=1
                                                duygusal_denge+=1
                                                aciklik-=1
                                                disa_donukluk-=1
                                                uyumluluk+=1
                                                
                                                #print("8 ->", neucount)
                                if str(ptweets)=='positive':
                                                postweet+=1
                                                sorumluluk-=1
                                                aciklik += 1
                                                disa_donukluk +=1
                                                uyumluluk+=1
                                                duygusal_denge+=1
                                                
                                                #print("9 ->", postweet)
                                if str(ptweets) == 'negative':
                                                
                                                negtweet+=1
                                                sorumluluk+=1
                                                aciklik+=1
                                                disa_donukluk-=1
                                                uyumluluk-=1
                                                duygusal_denge-=1
                                                
                                                #print("10 ->", negtweet)
                                                
                              #  print("counter:",self.counter," tweet sentiment:",parsed_tweet['sentiment'],"hashtag sentiment",ptweets)
                                
                def get_tweet_sentiment(self,tweet):
                    # Dışarıdan ulaşılmasını istediğimiz her fonksiyona self parametresini eklememiz gerekmektedir.
                    # Konuşma bölümü etiketleme, isim öbeği çıkarma, duygu analizi, sınıflandırma, çeviri ve daha fazlası gibi ortak doğal dil işleme (NLP) görevlerine dalmak için bir API sağlar.
                    # Burada TextBlob methoduna bir text nesnesi veririz, TextBlob bizi uğraştırmadan bu nesneyi bir dil işlemeden geçirir. Yani kelime köklerini bölmek, yanlış yazılmış kelimeleri düzeltmek vs.
                    # Bununla kalmaz, kendi datasetindeki kelimelere göre bir duygu polarite ölçümü de sağlar bizim için.
                                analysis = TextBlob(self.clean_tweet(tweet))
                                if analysis.sentiment.polarity > 0:
                                                #print("positive")
                                                return 'positive'
                                elif analysis.sentiment.polarity == 0:
                                                return 'neutral'
                                else:
                                                return 'negative'
                                                
                def get_tweets(self,query,count):
                                tweets1 = []
                                try:
                                                ptweets=0
                                                ntweets=0
                                                neut=0
                                                # q değişkeni altındaki twit sayısını al..
                                                # tweetleri almak için twitter api çağırılır.
                                                fetched_tweets = api.search(q = query, count = count)
                                                # tweetleri tek tek parse ediyoruz.
                                                for tweet in fetched_tweets:
                                                    # her tweetin bir metnini diziye ekle.
                                                                parsed_tweet = {}
                                                                #non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
                                                                parsed_tweet['text'] = tweet.text.translate(non_bmp_map) #tweet metnini almak.
                                                                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) #tweete ait duygu analazinin polaritesini almak.
                                                                if tweet.retweet_count > 0:
                                                                    # tweet'in retweetleri varsa, yalnızca bir kez eklendiğinden emin oluyoruz.
                                                                    # buradaki koşul aracalığıyla parse ettiğimiz tweeti, tweets listelesine ekleyeceğiz.
                                                                                if parsed_tweet not in tweets:
                                                                                                if parsed_tweet['sentiment']=='positive':
                                                                                                                ptweets+=1
                                                                                                elif parsed_tweet['sentiment']=='negative':
                                                                                                                ntweets+=1
                                                                                                else:
                                                                                                                neut+=1
                                                                                                tweets1.append(parsed_tweet)
                                                                else:
                                                                                if parsed_tweet['sentiment']=='positive':
                                                                                                ptweets+=1
                                                                                elif parsed_tweet['sentiment']=='negative':
                                                                                                ntweets+=1
                                                                                else:
                                                                                                neut+=1
                                                                                tweets1.append(parsed_tweet)
                                                                                #print(ptweets," ",ntweets," ",neut)
                                                if len(tweets1)==0:
                                                                return "0" ##ortada bir elde edilmiş bir twit yok demektir.
                                                if ptweets >= ntweets and ptweets >=neut  :
                                                                return "positive"
                                                elif ntweets >= ptweets and ntweets >=neut:
                                                                return "negative"
                                                else:
                                                                return "neutral"
                                                
                                
                                except tweepy.TweepError as e:
                                                print("Hata : " + str(e))
                                                return 0
                                

                def clean_tweet(self, tweet):
                                          return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
                                
                
class Grammar(threading.Thread): #Kullanıcının yazdığı twitler dil işlemeden geçirilir ve yazdığı tweetin dil bilgisi bakımından ne kadar doğru olduğu ölçüsüdür
                def __init__(self,counter,tweet):
                                threading.Thread.__init__(self)
                                self.counter=counter
                                self.tweet=tweet
                def clean_tweet(self,tweet):
                                return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

                def run(self):
                                try:
                                                global grammar
                                                self.tweet=self.clean_tweet(self.tweet) #temizlediğimiz twitleri aldık.
                                                p=parser.parse(self.tweet) #burada aldığımız twitleri dil işlemeden geçiyoruz.
                                                #print (p)
                                                if len(p['corrections'])<=2: #eğer dil işlemede düzeltme sayısı 2'den küçük-eşitse grammer bakımından doğru bir cümle olarak kabul ediyoruz bunu.
                                                                grammar+=1
                                except Exception as e:
                                                pass
                                                #print(e)
                
class Var(object):
        def __init__(self):                     
                self.agree=0
                self.opti = 0
                self.pessi = 0
                self.crit = 0
                self.neu = 0
                self.social = 0
                self.view = 0
                self.gram=0
                self.aciklik=0
                self.sorumluluk=0
                self.disa_donukluk=0
                self.uyumluluk=0
                self.duygusal_denge=0
                self.public=''
                self.subj=''
                self.img=''
                self.follower=0
                self.following=0
                self.tweets=0
                self.name=""
                self.yes="yes"
                self.t=[]
        def clean_tweet(self,tweet):
                return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
        def get_tweet_sentiment(self,tweet):
            # Dışarıdan ulaşılmasını istediğimiz her fonksiyona self parametresini eklememiz gerekmektedir.
            # Konuşma bölümü etiketleme, isim öbeği çıkarma, duygu analizi, sınıflandırma, çeviri ve daha fazlası gibi ortak doğal dil işleme (NLP) görevlerine dalmak için bir API sağlar.
            # Burada TextBlob methoduna bir text nesnesi veririz, TextBlob bizi uğraştırmadan bu nesneyi bir dil işlemeden geçirir. Yani kelime köklerini bölmek, yanlış yazılmış kelimeleri düzeltmek vs.
            # Bununla kalmaz, kendi datasetindeki kelimelere göre bir duygu polarite ölçümü de sağlar bizim için.
                analysis = TextBlob(clean_tweet(tweet))
                if analysis.sentiment.polarity > 0:
                        return 'positive'
                elif analysis.sentiment.polarity == 0:
                        return 'neutral'
                else:
                        return 'negative'
        def get_all_tweets(self):
                screen_name=self.subj #kullanıcı adı
                #Twitter, bu yöntemle yalnızca en yeni 3240 tweet'e erişim sağlar.
                #Tüm tweetleri bir listede tutmak için.
                new_tweets = []
                alltweets = []
               
                
                #en son tweetler için ilk istekte bulun (200, izin verilen maksimum sayıdır)
                try:
                                new_tweets = api.user_timeline(screen_name = screen_name,count=200) #tweetleri çekmek için api'ye ulaşıp kullanıcı adını ve sayısını kullanıyoruz.
                                alltweets.extend(new_tweets) #alltweets listesine ekledik.
                                oldest = alltweets[-1].id - 1 #id, o indexe ait nesnenin benzersiz kimliğini göstermektedir bize. Aslında bellek adresi gibi düşünebiliriz.
                                #Negatif indexler, sol yerine sağdan saydığınız anlamına gelir. Dolayısıyla,  alltweets[-1] son öğeyi, bellekteki adresini, -1 bir ise bir önceki adresi oldest değişkenine yazdırdığımızı görüyoruz.
                except Exception as e:
                                self.yes="no"
                                print(e)
                                return
                #en son tweetleri kaydet

                #en eski tweet'in kimliğini daha kaydet
                
                #alınacak tweet kalmayıncaya kadar tweetleri almaya devam et
                while len(new_tweets) > 0:
                                
                                #sonraki tüm istekler yinelemeleri önlemek için max_id parametresini kullanır
                                new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
                                
                                #en son tweetleri kaydet.
                                alltweets.extend(new_tweets)
                                
                                #en eski tweetlin kimliğini güncelliyoruz.
                                oldest = alltweets[-1].id - 1
                                
                                print ("...%s tweet şu ana kadar yüklendi." % (len(alltweets)))
                                
                                if(len(alltweets)>=100):
                                                break
                
                #tweepy, tweetleri csv'yi dolduracak bir 2D diziye dönüştürür.
                now = datetime.date.today()
                week=now-datetime.timedelta(days=15)
                #week=week.strftime('%d-%m-%Y')
                #print(now," ",str(week))
                socialbird=0
                outtweets = [[ tweet.text.encode("utf-8")] for tweet in alltweets]
                timetweet = [[ tweet.created_at] for tweet in alltweets]
                c=0
                #buradaki amacımız kullanıcının 15 günlük tweet akışını izlemektir. bu bize twiter'da ne kadar aktif olduğunu gösterecek olan etkidir.
                for tweet in timetweet:
                                if c>=50:
                                    break
                                tweet=str(tweet)
                                tweet=self.clean_tweet(tweet)
                                tweet=tweet.split(" ")
                                #tweet=tweet[4]+"-"+tweet[3]+"-"+tweet[2]
                                #print(tweet)
                                c+=1
                                #if int(tweet[2])>=int(week.strftime('%Y')):
                                    #if int(tweet[3])>=int(week.strftime('%m')):
                                        #if int(tweet[4])>=int(week.strftime('%d')):
                                                #socialbird+=1
                                
                                
                hashed=[]
                hashtweet=[]
                nohash=[]
                #print("SocialBird:{}/100".format(100*socialbird/len(timetweet)))
                for line in outtweets:
                                line=str(line)
                                """
                                Normal İfadelerle Arama (RegEx) Normal ifade, belirli terim ve ifadelerin aksine belirli kalıpları arayan gelişmiş bir arama şeklidir.
                                RegEx ile, birden çok değişmez arama sorgusu oluşturmak yerine belirli karakter dizelerini aramak için desen eşleştirmeyi kullanabiliriz.
                                Burada hashtag harici karakterleri alıyoruz.
                                """
                                search=re.search(r'^(.*)#(.*)\s*(.*)$',line) #Eğer twitin içinde hashtag varsa bütün hashtag harici bütün ifadeleri al. ama yoksa, hiçbir ifadeyi alma.
                                if(search): #hashtagli bir twitse
                                                search=str(line) #eğer search'ün içinde ifade varsa, gelen twiti içine atıyoruz.
                                                temp=(re.findall(r'[#]\S*',search)) #findall () modülü, belirli bir desene uyan “all” oluşumlarını aramak için kullanılır.
                                                # findall (), dosyanın tüm satırlarını tekrarlar ve üst üste binmeyen tüm kalıp eşleşmelerini tek bir adımda döndürür.
                                                t=self.clean_tweet(temp[0])
                                                hashtweet.append(t) #hashtag'i append ediyoruz.
                                                #print(t)
                                                hashed.append(line) #hashtag harici metni.
                                else: #hashtagsiz bir twitse
                                        line=self.clean_tweet(line)
                                        nohash.append(line)                                                
                                                                                
                try:
                                global agreecount,opticount,negtweet,critcount,pessicount,postweet,viewholdercount,neuttweet,neucount,viewtweet,grammar,aciklik,sorumluluk,disa_donukluk,uyumluluk,duygusal_denge,tweets
                                tweets=[]
                                agreecount=0
                                opticount=0
                                negtweet=0
                                critcount=0
                                pessicount=0
                                postweet=0
                                viewholdercount=0
                                neuttweet=0
                                neucount=0
                                viewtweet=0
                                grammar=0
                                aciklik = 0
                                sorumluluk = 0
                                disa_donukluk = 0
                                uyumluluk = 0
                                duygusal_denge = 0
                                #print ("Deneme", len(hashed))
                                threads=[]
                                counter=0
                                for tweet in hashed: #hashlenmiş twitlerin içini gez.
                                                if counter>=50:
                                                                break
                                                #threading.Thread(target=get_all_tweets, args=("Thread-2","elonmusk"))
                                                p=myThread(counter,str(tweet),hashtweet[counter])  #Thread class'ımıza gidiyoruz.
                                                p.start() #Thread işlemini başlatmak için.
                                                threads.append(p)
                                                counter+=1
                                
                                for t in threads:
                                           t.join() #Join () yöntemi bir dize yöntemidir ve dizi öğelerinin str ayırıcısı ile birleştirildiği bir dize döndürür.
                                           print ("#",end=' ')
                                print ()

                                counter=0
                                grammy=[]
                                for tweet in nohash:
                                                if counter>=50:
                                                        break
                                                p=Grammar(counter,str(tweet)) #Twitlerin dilbilgisi doğruluğu için dil işlemden geçirdiğimiz fonksiyona gönderiyoruz.
                                                p.start()
                                                grammy.append(p)
                                                counter+=1
                                for t in grammy:
                                                t.join()
                                                print("-",end=' ')
                                print()

                                                           
                except tweepy.TweepError as e:
                                print("Hata : "+str(e))
                #ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
                #print("Pozitif tweet yüzdesi : {} %".format(100*len(ptweets)/len(hashed)))
                #csv'yi yaz.
                if len(threads)==0: #thread işlemi olmadıysa
                    print ("Uygunluk:",agreecount," %")
                    self.agree=agreecount   
                else:
                    print("Uygunluk Yüzdesi:{} %".format(100*agreecount/len(tweet)))
                    print(agreecount)
                    self.agree = int(100*agreecount/len(tweet))
                    
                if len(threads)==0: #thread işlemi olmadıysa
                    print("Deneyime Açıklık Yüzdesi: ", aciklik, " %")
                    self.aciklik = aciklik
                else:
                    print("Deneyime Açıklık Yüzdesi:{} %".format(100*aciklik/len(tweet)))
                    print(aciklik)
                    self.aciklik = int(100*aciklik/len(tweet))
                    
                if len(threads)==0: #thread işlemi olmadıysa
                    print("Sorumluluk Yüzdesi: ", sorumluluk, " %")
                    self.sorumluluk = sorumluluk
                else:
                    print("Sorumluluk Yüzdesi:{} %".format(100*sorumluluk/len(tweet)))
                    print(sorumluluk)
                    self.sorumluluk = int(100*sorumluluk/len(tweet))

                if len(threads) == 0:  # thread işlemi olmadıysa
                    print("Dışa Dönüklük: ", disa_donukluk, " %")
                    self.disa_donukluk = disa_donukluk
                else:
                    print("Dışa Dönüklük:{} %".format(100 * disa_donukluk / len(tweet)))
                    print(disa_donukluk)
                    self.disa_donukluk = int(100 * disa_donukluk / len(tweet))
                    
                if len(threads) == 0:  # thread işlemi olmadıysa
                    print("Uyumluluk: ", uyumluluk, " %")
                    self.uyumluluk = uyumluluk
                else:
                    print("Uyumluluk:{} %".format(100 * uyumluluk / len(tweet)))
                    print(uyumluluk)
                    self.uyumluluk = int(100 * uyumluluk / len(tweet))
                    
                if len(threads) == 0:  # thread işlemi olmadıysa
                    print("Duygusal Denge: ", duygusal_denge, " %")
                    self.duygusal_denge = duygusal_denge
                else:
                    print("Duygusal Denge:{} %".format(100 * duygusal_denge / len(tweet)))
                    print(duygusal_denge)
                    self.duygusal_denge = int(100 * duygusal_denge / len(tweet))

                
                if len(threads)==0:
                    self.pessi=0
                    print("Kötümserlik:0 %")
                elif negtweet==0 or pessicount==0:
                                ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] #alınan twitlerin içinde negatif olanları seç.
                                print("Kötümserlik-{} %".format(100*len(ptweets)/len(threads)))
                                self.pessi = int(100*len(ptweets)/len(threads))
                                print(pessicount)
                else:
                                print("Kötümserlik Yüzdesi:{} %".format(100*pessicount/negtweet))
                                self.pessi = int(100*pessicount/negtweet)
                                print(pessicount)

                if len(threads)==0:
                    self.view=0
                    print("Farklılık:0%")
                elif viewtweet==0:
                        ptweets = [tweet for tweet in tweets if tweet['sentiment'] != 'neutral']
                        print("Farklılık:{} %".format(100 * len(ptweets) / len(threads)))
                        self.view = int(100 * len(ptweets) / len(threads))
                        print(viewholdercount)
                else:
                        print("Farklılık Yüzdesi-{} %".format(100*viewholdercount/viewtweet))
                        self.view = int(100 * viewholdercount / viewtweet)
                        print(viewholdercount)


                if len(threads)==0:
                    self.neu=0
                    print("Tarafsızlık:0%")
                elif neuttweet!=0:
                                print("Tarafsızlık:{} %".format(100*neucount/neuttweet))
                                self.neu = int(100*neucount/neuttweet)
                                print(neucount)
                else:
                                neut=[tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
                                print("Tarafsızlık:{} %".format(100*len(neut)/len(threads)))
                                self.neu = int(100*len(neut)/len(threads))
                                print(neucount)

                self.follower=api.get_user(screen_name).followers_count
                self.following=api.get_user(screen_name).friends_count
                print("takipçiler-",self.follower)
                print("takip ettiklerin-",self.following)
                self.img=api.get_user(screen_name).profile_image_url
                self.img=self.img.replace("_normal",'')
                #print(x)
                print(self.img)
                #print("listed in-",api.get_user(screen_name).listed_count)
                if(api.get_user(screen_name).verified):
                                print("Tanınmış Bir Kişi")
                                self.public="Tanınmış Bir Kişi"
                else:
                                print("Tanınmış Bir Kişi Değil")
                                self.public="Tanınmış Bir Kişi Değil"
                if len(timetweet)==0:
                    print("Aktiflik-",socialbird,"%")
                    self.social=socialbird
                else:
                    print("Aktiflik:{} %".format(100*socialbird/len(timetweet)))
                    self.social = int(100*socialbird/len(timetweet))
                
                if len(nohash)==0:
                        print("Dil Bilgisine Önem:0%")
                        self.gram=0
                else:
                        print("Dil Bilgisine Önem:{}%".format(100*grammar/counter))
                        self.gram = int(100*grammar/counter)
                self.tweets=api.get_user(screen_name).statuses_count
                print("tweet sayısı:",self.tweets)
                self.name=api.get_user(screen_name).name
                print (self.name)
                self.t=tweets
                #print (str(now.date))
                return self








  






