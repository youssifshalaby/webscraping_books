import requests
from bs4 import BeautifulSoup
import pandas as pd
data = []
current_page = 1
while(True):

  page = requests.get(f"https://books.toscrape.com/catalogue/page-{current_page}.html")
  soup = BeautifulSoup(page.content, "lxml")

  if soup.title.text == "404 Not Found":
    break
  books = soup.find_all("article",class_="product_pod")
  for book in books:
    item = {}
    item["title"] = book.find("img").attrs["alt"]
    item["price"] = book.find("p",class_="price_color").text[1:]
    item["available"] = book.find("p",class_='instock').text.strip()
    item["link"] = book.find("a").attrs["href"]
    data.append(item)
  current_page += 1
df = pd.DataFrame(data)
df.to_csv("books.csv")