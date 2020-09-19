import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.it/Apple-iPhone-11-64GB-Nero/dp/B07XS2ZR1K/ref=sr_1_5?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=iphone+11&qid=1600534359&sr=8-5'

# YOUR_IDEAL_PRICE = int(input("please enter the idel price for you :"))

# PLEASE REPLACE THIS CODE WITH YOUR USER AGENT :
# TO GET YOUR USER AGENT GO TO YOUR BROWSER AND SEARCH FOR "MY USER AGENT" AND REPLACE IT WITH YOURS.
headers = {"user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

page = requests.get(URL,headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price =  price[0:5]

print(float(converted_price))
