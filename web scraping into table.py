import urllib.request
import pandas as pd

url = "https://www.webscraper.io/test-sites/tables/tables-without-thead"

with urllib.request.urlopen(url) as i:
    html = i.read()


data = pd.read_html(html)[0]
# data.to_csv("programming.csv")
print(data.to_string())