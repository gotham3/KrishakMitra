# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.conf.urls import url
from .views import login_view, register_user,logout_view

#from django.contrib.auth.views import LogoutView

urlpatterns = [
    url('login/', login_view, name="login"),
    url('register/', register_user, name="register"),
    url("logout/",logout_view, name="logout")
]
