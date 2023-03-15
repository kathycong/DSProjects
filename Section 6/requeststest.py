#Introduction to Request
#pip3 install requests
#pip3 install pillow

import requests
from  io import BytesIO
from PIL import Image

r = requests.get("https://wallpapercave.com/wp/TuVhQdr.jpg")

print("Status:", r.status_code) #returns status code 200 which refers to OK

#creating an image from the binary data that we get
image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./Section 6/image" + image.format


#saving the image into local directory

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")


