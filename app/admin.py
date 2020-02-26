# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import UserProfile,Advertisement
admin.site.register(UserProfile)
admin.site.register(Advertisement)
# Register your models here.
