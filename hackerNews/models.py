# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class HackerNews(models.Model):

    POSITIVE_SENTIMENT = 0
    NEGATIVE_SENTIMENT = 1
    NEUTRAL_SENTIMENT = 2

    sentiment_choices = [
        (POSITIVE_SENTIMENT, "Positive"),
        (NEGATIVE_SENTIMENT, "Negative"),
        (NEUTRAL_SENTIMENT, "Neutral"),
    ]

    hacker_id = models.IntegerField(db_index=True, null=False)
    user_name = models.CharField(max_length=30)
    article_title = models.CharField(max_length=40, db_index=True)
    article_url = models.URLField()
    article_score = models.IntegerField()
    article_description = models.TextField()
    sentiment = models.SmallIntegerField(choices=sentiment_choices)

    def get_sentiment(self, sentiment_text):
        
        for sentiment in self.sentiment_choices:
            print sentiment[1].lower(), " and ", sentiment_text.lower(), sentiment[1].lower() == sentiment_text.lower()
            if sentiment[1].lower() == sentiment_text.lower():
                return sentiment[0]
        return self.NEUTRAL_SENTIMENT

    def __str__(self):
        return self.article_title
