from bs4 import BeautifulSoup
import requests
from PIL import Image #used for importing images
from io import BytesIO
import os

def StartSearch():
    search = input("search for:")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    r = requests.get("http://www.bing.com/images/search", params = params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        img_obj = requests.get(item.attrs["href"])
        print("Getting", item.attrs["href"])
        #getting the title of the image
        title = item.attrs["href"].split("/")[-1] #getting the last element of the list using -1
        try:
            img = Image.open(BytesIO(img_obj.content))
            img.save("./" + dir_name + "/" + title, img.format)
        except:
            print("Could not save image")
    
    StartSearch()
StartSearch()