# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HackerNews(models.Model):

    POSITIVE_SENTIMENT = 0
    NEGATIVE_SENTIMENT = 1

    sentiment_choices = [
        (POSITIVE_SENTIMENT, "Positive"),
        (NEGATIVE_SENTIMENT, "Negative"),
    ]

    hacker_id = models.IntegerField(db_index=True, null=False)
    user_name = models.CharField(max_length=30)
    article_title = models.CharField(max_length=40)
    article_url = models.URLField()
    article_score = models.IntegerField()
    article_description = models.TextField()
    sentiment = models.SmallIntegerField(choices=sentiment_choices)