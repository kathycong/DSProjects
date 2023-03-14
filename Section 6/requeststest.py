#Introduction to Request
#pip3 install requests

import requests

r = requests.get("http://google.com")
print("Status:", r.status_code) #returns status code 200 which refers to OK
print(r.url) #getting the url

#note:
#HTTP Status codes provides a description of each code
#https://www.restapitutorial.com/httpstatuscodes.html

#getting the content of the url
print(r.text)

#loading file into html
f = open("./Section 6/page.html", "w+") #write mode
f.write(r.text)

