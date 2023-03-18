import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.mydb
Users = db.users
Users.find().count()

#counting documents given with below criteria
Users.find({"favorite_number": 445}).count()

#using multiple field and values to find a document
Users.find({"favorite_number": 445, "username":"yetanother"}).count()

#Datetime and Keyword with Pymongo
import datetime #a base package

current_date = datetime.datetime.now()
current_date

old_date = datetime.datetime(2009, 8, 11)
uid = Users.inser({"username": "file", "date": current_date})

#find users 
#$gt refers to greater than
Users.find({"date": {"$gt" : old_date}}).count()
#$lt refers to less than
Users.find({"date": {"$lt" : old_date}}).count()

Users.find({"date": {"$exists" : True}}).count()

#find any documents that is not equal to yetanother using $ne which means notequal
Users.find({"date": {"$ne" : "yetanother"}}).count()

