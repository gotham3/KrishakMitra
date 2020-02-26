# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.conf.urls import url,include
urlpatterns = [
    url('admin/', admin.site.urls),
    url("", include(('authentication.urls', 'authentication'), namespace="authentication")), # add this
    url("", include(('app.urls', 'app'), namespace="app")), # add this
]
