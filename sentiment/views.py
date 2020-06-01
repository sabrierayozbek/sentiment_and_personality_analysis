from django.shortcuts import get_object_or_404, redirect, render
from .forms import Query
from .sentiment import TwitterObject
from django.http import HttpResponseRedirect

#Django web uygulamaları genellikle bu adımların her birini işleyen kodu ayrı dosyalarda gruplandırır:
#https://i.stack.imgur.com/pv75H.png
"""
URLs: Her bir URL'den gelen istekleri tek bir işlevle işlemek mümkün olsa da, her kaynağı işlemek için ayrı bir görünüm işlevi yazmak çok daha kolaydır.
HTTP isteklerini, istek URL'sini temel alarak uygun görünüme yönlendirmek için bir URL eşleyici kullanılır.
URL eşleyici ayrıca bir URL'de görünen belirli dizeler veya rakam kalıplarıyla eşleşebilir ve bunları veri olarak bir görüntüleme işlevine geçirebilir.

Views: Görünüm, HTTP isteklerini alan ve HTTP yanıtlarını döndüren bir istek işleyici işlevidir.
Görünümler, modeller aracılığıyla istekleri karşılamak ve şablonlara yanıtın biçimlendirilmesini temsil etmek için gereken verilere erişir.

Models: Modeller, bir uygulamanın verilerinin yapısını tanımlayan ve veritabanındaki kayıtları yönetmek (eklemek, değiştirmek, silmek) ve sorgulamak için mekanizmalar sağlayan Python nesneleridir.

Templates: Şablon, gerçek içeriği temsil etmek için kullanılan yer tutucularla bir dosyanın (HTML sayfası gibi) yapısını veya düzenini tanımlayan bir metin dosyasıdır.
 Bir görünüm, HTML şablonunu kullanarak bir modeldeki verilerle doldurarak dinamik olarak bir HTML sayfası oluşturabilir. Herhangi bir dosya türünün yapısını tanımlamak için bir şablon kullanılabilir;
 HTML olması gerekmez!

"""


"""
Belirli bir şablonu belirli bir bağlam sözlüğüyle birleştirir ve bu oluşturulan metinle birlikte bir HttpResponse nesnesi döndürür.

Django, TemplateResponse yapıcısı render () ile aynı düzeyde kolaylık sunduğundan bir TemplateResponse döndüren bir kısayol işlevi sağlamaz.
"""

"""
Daha fazla bilgi için; https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/
"""



def firstPage(request): #Bu yanıtı oluşturmak için kullanılan istek nesnesi.
	return render(request, 'first.html')


def home(request): #Bu sayfada kullanıcının adını yazarak bir post isteğinde bulunmuş oluyoruz.
	form = Query(request.POST or None)
	context = {
		'form': form,
	}
	if form.is_valid():
		request.session['form'] = request.POST
		return HttpResponseRedirect('tweetView')
	return render(request, 'home.html', context)


def tweetView(request): #tweetleri gösterdiğimiz sayfanın içerisindeyiz.
	form = Query(request.session.get('form'))
	obj = TwitterObject()
	posTweet = []
	negTweet = []
	neutTweet = []
	posPer = 0
	negPer = 0
	neutPer = 0
	context = {
		'posTweet': posTweet,
		'negTweet': negTweet,
		'neutTweet': neutTweet,
		'posPer': posPer,
		'negPer': negPer,
		'neutPer': neutPer,
	}
	if form.is_valid():
		obj = TwitterObject()
		obj.subj = request.session.get('form')['Query']
		obj.fetchTweets()
		ptweets = obj.ptweets
		ntweets = obj.ntweets
		neutral = obj.neutral
		
		total = len(ptweets) + len(ntweets) + len(neutral)
		posPer = format(100 * len(ptweets) / total) #pozitif, negatif ve nötr twit yüzdeleri
		negPer = format(100 * len(ntweets) / total)
		neutPer = format(100 * len(neutral) / total)
		
		# Pozitif
		for tweet in ptweets[:20]:
			posTweet.append(tweet['text'])
		# Negaitif
		for tweet in ntweets[:20]:
			negTweet.append(tweet['text'])
		# Neutral
		for tweet in neutral[:20]:
			neutTweet.append(tweet['text'])
	
	context = {
		'posTweet': posTweet,
		'negTweet': negTweet,
		'neutTweet': neutTweet,
		'posPer': posPer,
		'negPer': negPer,
		'neutPer': neutPer,
	}
	return render(request, 'tweetView.html', context)


