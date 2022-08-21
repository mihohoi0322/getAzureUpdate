import urllib.parse
import feedparser
import pandas as pd

urls = ""
def getrss(month, category, *args):
    global urls
    categories = {"category": category}

    for key in args:
        if not urls:
            urls = "," + key
        else:
            urls = urls + "," + key

    html = "https://azure.microsoft.com/ja-jp/updates/feed" + "?" + urllib.parse.urlencode(categories) + urls
    print(html)
    lists = feedparser.parse(html)
    print(lists.entries)
    file = open("test.csv", "w")

    rss_list = []
    for rss in lists.entries:
        dic = {
            "title": rss.title,
            "link": rss.link,
            "summary": rss.summary,
            "year": rss.published_parsed.tm_year,
            "month": rss.published_parsed.tm_mon,
            "day": rss.published_parsed.tm_mday,
        }
        rss_list.append(dic)

    filterMonth(month, rss_list)
    return

def filterMonth(month, rss_list):
    df = pd.json_normalize(rss_list)
    df = df[(df['month'] == month) & (df['year'] == 2022)]

    df.to_csv('test.csv', index=False)
    return

rss_list = getrss(8, "databases", "compute", "identity")
