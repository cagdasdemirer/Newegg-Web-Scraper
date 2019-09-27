from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client


page_url = input("Enter your URL:   ")

uClient = uReq(page_url)


page_soup = soup(uClient.read(), "html.parser")
uClient.close()

containers = page_soup.findAll("div", {"class": "item-container"})

out_filename = "results.csv"
headers = "brand,product_name,shipping \n"

f = open(out_filename, "w")
f.write(headers)

for container in containers:
    make_rating_sp = container.div.select("a")
    brand = make_rating_sp[0].img["title"].title()
    product_name = container.div.select("a")[2].text
    shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

    print("brand: " + brand + "\n")
    print("product_name: " + product_name + "\n")
    print("shipping: " + shipping + "\n")

    f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")

f.close()
