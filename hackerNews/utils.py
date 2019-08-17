import requests
import json
import os

HACKER_NEWS_API_HOST = "https://hacker-news.firebaseio.com"
API_VERSION = "v0"
JSON_FILE_EXT = ".json"


def get_url(file_location):
    return "{}/{}/{}{}?print=pretty".format(HACKER_NEWS_API_HOST, API_VERSION, 
    file_location, JSON_FILE_EXT)


def send_request_for_article(url, method, payload, headers={}):
    return requests.request(method, url, data=payload, headers=headers)


def get_top_news():
    url = get_url("topstories")
    payload = {}
    response = send_request_for_article(url, "GET", payload)
    return json.loads(response.text)


def get_item_details(hacker_id):
    url = get_url("item/{}".format(hacker_id))
    payload = {}
    response = send_request_for_article(url, "GET", payload)
    return json.loads(response.text)


def get_sentiment(input_text):
    from aylienapiclient import textapi
    client = textapi.Client("91717892", "e89770abfbf50ce1b8b314be1f730666")
    sentiment = client.Sentiment({'text': input_text.encode('utf-8')})
    return sentiment



