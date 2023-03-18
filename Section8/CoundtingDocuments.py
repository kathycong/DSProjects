import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.mydb
Users = db.users
Users.find().count()

#counting documents given with below criteria
Users.find({"favorite_number": 445}).count()