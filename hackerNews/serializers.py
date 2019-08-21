from rest_framework import serializers
from .models import HackerNews


class HackerNewsSerializer(serializers.HyperlinkedModelSerializer):

    sentiment = serializers.SerializerMethodField()

    class Meta:
        model = HackerNews
        fields = ['hacker_id', 'user_name', 'article_title', 'article_url',
            'article_score', 'article_description', 'sentiment'
        ]

    def get_sentiment(self, obj):
        return obj.get_sentiment_display()