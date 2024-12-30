from Korpora import Korpora
modu_news = Korpora.load('modu_news', force_download=True)
print(modu_news[0])