import lxml.etree

rss = lxml.etree.parse("https://azurecomcdn.azureedge.net/ja-jp/updates/feed/")
root = rss.getroot()


