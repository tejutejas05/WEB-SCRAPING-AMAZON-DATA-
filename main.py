from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML file
with open("amazon.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

products = []

# Find all divs with class sg-col-inner
divs = soup.find_all("div", class_="sg-col-inner")

for div in divs:
    name = ""
    price = ""

    # Find product name
    title_tag = div.find("span", class_="a-size-medium a-spacing-none a-color-base a-text-normal")
    if title_tag:
        name = title_tag.get_text(strip=True)

    # Find price
    price_tag = div.find("span", class_="a-price-whole")
    if price_tag:
        price = price_tag.get_text(strip=True)

    # Store only if name exists
    if name:
        products.append([name, price])

# Convert to DataFrame
df = pd.DataFrame(products, columns=["Product Name", "Price"])

# Save to Excel
df.to_excel("amazon_products.xlsx", index=False)

print("✅ Data saved to amazon_products.xlsx")