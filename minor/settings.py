"""
Django settings for minor project.

Bu linkte daha fazla bilgi bulunabilir.
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Bu şekilde, loglar artık Django projeleri için manage.py dosyasını içeren dizine ayarlanan BASE_DIR değişkenine göre bir konuma yazılır.
#Projenin içinde şu şekilde yollar oluşturabiliriz: os.path.join (BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Başlangıç ayarlarının referans alındığı kısım aşağıdadır.
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

#  Secret key, gizli ve rastgele bir değerdir.
SECRET_KEY = 'g1w6+lk9l+g#oc6-c-c$w#xpv3s)2)#^+pn446jxx#4h2(q*r#'

#Debug true ve allowed_hosts boş olduğunda, ana bilgisayar ['localhost', '127.0.0.1', '[::1]'] ile doğrulanır.
DEBUG = True

ALLOWED_HOSTS = []


# Uygulamanın tanımlamaları.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    #'django.contrib.staticfiles',
    'sentiment',
    'personality',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'minor.urls' #Root URL'mizi Python'da içe aktarma yolunu temsil eden bir dizi.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'minor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases linki referans alınmıştır.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), #URL yönlendirmesi.
    }
}




# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

