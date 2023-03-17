#pip3 install bs4 #installing beautiful soup

from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")
params = {"q": search}
r = requests.get("http://www.bing.com/search", params = params)

soup = BeautifulSoup(r.text)
print(soup.prettify())
