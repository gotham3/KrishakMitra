# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

#from django.urls import re_path
from app import views
from django.conf.urls import url
urlpatterns = [
    # Matches any html file 
    #re_path(r'^.*\.html', views.pages, name='pages'),
    url('new_ad/', views.ad, name='ad'),
    url('profile/', views.profile, name='profile'),
    url('home/', views.home, name='home'),
    url('ads/',views.ads_list,name="ads_list"),
    url('complaint/',views.complaint_view,name = "complaint"),
    url('billing/(?P<pk>\d+)/', views.billing, name = "billing"),
    url('',views.starting_page,name = "starting_page"),
    
    
]
