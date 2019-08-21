# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import HackerNews

# Register your models here.
class HackerNewsAdmin(admin.ModelAdmin):
    list_filter = ['sentiment']

admin.site.register(HackerNews, HackerNewsAdmin)