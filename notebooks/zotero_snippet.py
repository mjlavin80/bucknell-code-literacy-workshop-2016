%matplotlib inline
import matplotlib.pyplot as plt
from pyzotero import zotero
from collections import Counter

library_id = "655084"
library_type = "group"
api_key= "Your API key here"

zot = zotero.Zotero(library_id, library_type, api_key)
hybrid_blended = zot.everything(zot.collection_items("95HW46ZG"))
dates = [int(i["data"]["date"]) for i in hybrid_blended]

years = [d for d in set(dates)]
years.sort()
counts = Counter([u for u in dates])
articles = [counts[y] for y in years]

plt.figure(figsize=(20,10))
plt.plot(years[4:], articles[4:])
plt.show()
