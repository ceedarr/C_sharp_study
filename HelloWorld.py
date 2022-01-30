import os
import bs4 from Beautifulsoup
import requests

url = "https://github.com/"
responce = requests.get(url)
print(responce.status_code)
