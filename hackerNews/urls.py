from django.conf.urls import url
from .views import get_news_articles


urlpatterns = [
    url(r'^$', get_news_articles, name="get_news_articles"),
]