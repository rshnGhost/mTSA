"""mobile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
#from mobile.account import views as core_views

#importing views
#we need to create views.py
from . import views
from mobile import views as mobileViews

urlpatterns = [
	#url(r'^adminPage/', admin.site.urls),
	#define the url getdata that we have written inside form
	url(r'^getdata/(?P<model>[\w-]+)/$', views.getdata),
	url(r'^getdata/(?P<model>[\w-]+)/data/$', views.showdata),
	#url(r'^getdata/', views.getdata),
	#defining the view for root URL
	#url(r'^$', views.index),

	#url(r'^$', auth_views.login, {'template_name': 'login.html'}),
	url(r'^$', mobileViews.index, name='home'),
	#url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	#url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
	#url(r'^signup/$', views.signup, name='signup'),
	#url(r'^verification/$', views.verification, name='verification'),
	#url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),

	url(r'^custom/$', views.customPut, name='cuGet'),
	url(r'^create/$', views.createTweet, name='crTwe'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
