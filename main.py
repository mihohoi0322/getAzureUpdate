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

def filterMonth(month):
    list(filter(lambda x: rss_list.sort(month = 8)))
    return


rss_list = getrss("containers")
print(rss_list)

df = pd.json_normalize(rss_list)

print(df[df['month'] == 8])
df = df[(df['month'] == 8) & (df['year'] == 2022)]

df.to_csv('test.csv', index=False)