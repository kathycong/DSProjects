#pip3 install bs4 #installing beautiful soup

from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")
params = {"q": search}
r = requests.get("http://www.bing.com/search", params = params)

soup = BeautifulSoup(r.text, "html.parser") #setting up the parser
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text #finding element a
    item_href = item.find("a").attrs["href"] #finding the attribute href of element a

    if item_text and item_href:
        print(item_text)
        print(item_href)
        #find the parent of the item
        print("Parent:", item.find("a").parent.parent.find("p").text)

        #find the children of item element
        children = item.find("h2")
        print("Next sibling of the h2:", children.sibling)



