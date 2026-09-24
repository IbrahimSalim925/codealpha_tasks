import requests
from bs4 import BeautifulSoup
import pandas as pd 

data = []
for page in range(1, 51):

    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books :
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        availability= book.find("p",class_="instock availability").text.strip()

        book_data = {
           "Title" : title,
           "Price" : price,
           "Rating" : rating,
           "Availability" : availability,
       }

        data.append(book_data)

df = pd.DataFrame(data)
df["Price"] = df["Price"].str.replace("Â£", "").astype(float)

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)
df = df.drop_duplicates()
df = df.dropna()
print(df.head())

df.to_csv("books.csv", index=False)


   
