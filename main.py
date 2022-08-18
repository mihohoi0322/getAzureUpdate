import urllib.parse
import feedparser
import pandas as pd

# TODO: list a category
def getrss(category):
    categories = {"category": category}
    html = "https://azure.microsoft.com/ja-jp/updates/feed" + "?" + urllib.parse.urlencode(categories)
    lists = feedparser.parse(html)

    file = open("test.csv", "w")

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

    return rss_list
# TODO: output a csv file use pandas

# TODO: filter to year & month
def filterMonth(month):
    list(filter(lambda x: rss_list.sort(month = 8)))
    return


rss_list = getrss("containers")
print(rss_list)
print(type(rss_list))
print(pd.json_normalize(rss_list))