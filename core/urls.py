"""skyettecareer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
import core.views as coreviews

urlpatterns = patterns('',

	url(r'^$', coreviews.LandingView.as_view()),
 	url(r'workplace/$', coreviews.WorkplaceListView.as_view()),
 	url(r'search/$', coreviews.SearchListView.as_view()),
 	url(r'workplace/(?P<pk>\d+)/detail/$', coreviews.WorkplaceDetailView.as_view(), name='workplace_list'),
 	url(r'workplace/create/$', coreviews.WorkplaceCreateView.as_view()),
 	url(r'workplace/(?P<pk>\d+)/update/$', coreviews.WorkplaceUpdateView.as_view(), name='workplace_update'),
 	url(r'workplace/(?P<pk>\d+)/review/create/$', coreviews.ReviewCreateView.as_view(), name='review_create'),
 	url(r'workplace/(?P<pk>\d+)/review/update/$', coreviews.ReviewUpdateView.as_view(), name='review_update'),
)
