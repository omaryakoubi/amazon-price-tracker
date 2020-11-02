import requests
from bs4 import BeautifulSoup
import smtplib 
import time

# URL = 'https://www.amazon.it/Apple-iPhone-11-64GB-Nero/dp/B07XS2ZR1K/ref=sr_1_5?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=iphone+11&qid=1600534359&sr=8-5'

URL = str(input("Enter the amazon product link here"))
user_ideal_price = int(input("Enter the ideal price for you:"))
user_email = str(input("Enter your email address:  "))

headers = {"user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

def check_price():
    page = requests.get(URL,headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    product_title = soup.find(id="productTitle").get_text()
    product_price = soup.find(id="priceblock_ourprice").get_text()
    converted_price =  float(product_price[0:5].replace(',','.'))

    if (converted_price < user_ideal_price):
        send_email()

def send_email() :
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("email","password")
    subject = "Price fell down!"
    body = f"Check the price on amazon {URL}"
    msg = f"subject:{subject}\n\n{body}"
    server.sendmail("email", user_email, msg)

    server.quit()

while(True):
    check_price
    time.sleep(60 * 60 * 60)