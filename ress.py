import urllib.parse
import feedparser


categories = {"category": "containers"}
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
    print(dic)

