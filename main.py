import urllib.parse
from bs4 import BeautifulSoup
import requests
import feedparser


def getRSS(category):
    categories = {"category": category}
    html = "https://azure.microsoft.com/ja-jp/updates/feed" + "?" + urllib.parse.urlencode(categories)
    lists = feedparser.parse(html)

    rss_list = []
    for rss in lists.entries:
        dic = {
            "title": rss.title,
            "link": rss.link,
            "summary": rss.summary,
            "year": rss.published_parsed.tm_year,
            "month": rss.published_parsed.tm_mon,
            "day": rss.published_parsed.tm_mday
        }
        rss_list.append(dic)
        print(rss_list)
    return rss_list

print(getRSS("container"))


