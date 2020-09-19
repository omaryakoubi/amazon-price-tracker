import requests
from bs4 import BeautifulSoup

URL = input('paste here the link of your amazon product: ')

# to get your user agent go to google and search for "my user agent".
headers = {"user-agent" : 'paste you user_agent here'}

page = requests.get(URL,headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')