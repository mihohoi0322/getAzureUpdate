import urllib.parse
from bs4 import BeautifulSoup
import requests
import feedparser
import pprint

category = {"category": "containers"}
html = "https://azure.microsoft.com/ja-jp/updates/feed" + "?" + urllib.parse.urlencode(category)
artuckes = feedparser.parse(html)


for rss in artuckes.entries:
    dic = {
        "title": rss.title,
        "link": rss.link,
        "summary": rss.summary,
        "year": rss.published_parsed.tm_year,
        "month": rss.published_parsed.tm_mon,
        "day": rss.published_parsed.tm_mday
    }
    print(dic)

