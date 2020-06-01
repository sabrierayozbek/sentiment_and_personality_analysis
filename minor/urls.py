"""minor URL Configuration

"Urlpatterns" listesi URL'leri yönlendirme görevi görür. Daha fazla bilgi için linki inceleyebilrsiniz:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache
from . import settings
import sentiment.views
import personality.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', sentiment.views.firstPage),
    url(r'^query$',sentiment.views.home),
    url(r'^tweetView$', sentiment.views.tweetView),
    url(r'^personquery/$', personality.views.home),
    url(r'^personquery/personAssess$', personality.views.personAssess),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, view=never_cache(serve))
