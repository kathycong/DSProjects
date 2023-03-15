import requests
import simplejson as json

#creating a payload of data which refers to data being sent to the URL
url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longurl": "http://example.com"}


headers = {"ContentType": "application/json" }

r = requests.post(url, json=payload)

print(r.headers)

print(json.loads(r.text)["error"]["code"])


