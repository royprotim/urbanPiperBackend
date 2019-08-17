# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import HackerNews
from .serializers import HackerNewsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from .utils import get_top_news, get_item_details, get_sentiment
from rest_framework.response import Response

@csrf_exempt
@api_view(['GET'])
def get_news_articles(request):

    ids = get_top_news()
    for ID in ids:
        try:
            hacker_news = HackerNews.objects.get(hacker_id=ID)
        except ObjectDoesNotExist:
            hacker_news_response = get_item_details(ID)
            # hacker_news = HackerNews()
            # hacker_news.hacker_id = ID
            # hacker_news.user_name = hacker_news_response.get("by", "Unknown Author")
            # hacker_news.article_title = hacker_news_response.get("title", "Unknown Title")
            # hacker_news.article_url = hacker_news_response.get("url", None)
            # hacker_news.article_score = hacker_news_response.get("score", None)
            # hacker_news.article_description = hacker_news_response.get("text", "No Text")
            print get_sentiment(hacker_news_response.get('title'))



    return Response({"message": "Yes!!!", "ids": ids})
