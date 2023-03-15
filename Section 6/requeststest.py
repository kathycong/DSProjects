import requests

my_data = {"name": "Kath", "email": "kath@example.com"}
r = requests.post("https://www.w3schools.com/php/welcome.php", data = my_data)

f = open("Section 6/myfile.html", "w+")
f.write(r.text)



