import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target website (example scraping site)
URL = "https://books.toscrape.com/"

# Send HTTP request
response = requests.get(URL)
response.raise_for_status()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

books_data = []

# Extract book information
books = soup.select("article.product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text
    rating = book.p["class"][1]  # Example: 'Three', 'Four'

    books_data.append({
        "title": title,
        "price": price,
        "rating": rating
    })

# Convert to DataFrame
df = pd.DataFrame(books_data)

# Save to CSV and JSON
df.to_csv("books.csv", index=False)
df.to_json("books.json", orient="records", indent=2)

print("Scraping completed. Data saved to books.csv and books.json")

