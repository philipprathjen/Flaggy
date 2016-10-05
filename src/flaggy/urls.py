"""flaggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
#from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from newsletter.views import home, contact
from flaggy.views import about
from profiles.views import profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='profile'),
    url(r'^contact$', contact, name='contact'),
    url(r'^about$', about, name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', profile, name='profile'),
] 
# It's taking these urls and then appending the static
# Doing it this way seperates development from what we would have in production, when DEBUG is off. 
if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)