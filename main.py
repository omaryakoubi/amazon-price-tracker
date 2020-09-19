import requests
from bs4 import BeautifulSoup

URL = input("paste here the link of your amazon product: ")

# PLEASE REPLACE THIS CODE WITH YOUR USER AGENT :
# TO GET YOUR USER AGENT GO TO YOUR BROWSER AND SEARCH FOR "MY USER AGENT" AND REPLACE IT WITH YOURS.
headers = {"user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

page = requests.get(URL,headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")
price = soup.find(id="priceblock_ourprice")

print(price)
