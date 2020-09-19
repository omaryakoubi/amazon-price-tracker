import requests
from bs4 import BeautifulSoup

URL = input("paste here the link of your amazon product: ")

# to get your user agent go to google and search for "my user agent".
headers = {"user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

page = requests.get(URL,headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")
price = soup.find(id="priceblock_ourprice")

print(price)
