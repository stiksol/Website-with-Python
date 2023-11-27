from eventregistry import *

YOUR_API_KEY = "c8bd46b5-db7f-4ce0-900c-72831d986dcb"
er = EventRegistry(apiKey=YOUR_API_KEY)

# get the USA URI
usUri = er.getLocationUri("USA")  # = http://en.wikipedia.org/wiki/United_States

q = QueryArticlesIter(
    keywords=QueryItems.OR(["George Clooney", "Sandra Bullock"]),
    minSentiment=0.4,
    sourceLocationUri=usUri,
    dataType=["news", "blog"])

# obtain at most 500 newest articles or blog posts, remove maxItems to get all
for art in q.execQuery(er, sortBy="date", maxItems=500):
    print(art)
