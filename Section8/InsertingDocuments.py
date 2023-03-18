#MongoDB is a NO SQL database

#installing it via terminal 'brew install mongodb'

# we need to start mongodb 'brew services start mongodb'

#connecting to mongodb client
#curl http://localhost:27017 

#install python package 
#pip3 install pymongocd

import pymongo
from pymongo import MongoClient

#setting up the client with default
myClient = MongoClient()

##creating a database
db = myClient.mydb #or myClient["mydatabase"]

##accessing the tables in the database
users =db.users

user1 = {"username": "nick", "password": "myverysecurepassword", "favoritenumber": 445, "hobbies": ["python", "games", "pizza"]}

#inserting users to database
user_id = users.insert_one(user1).inserted_id

user1 = {"username": "anothe_user", "password": "myverysecurepassword", "favoritenumber": 445, "hobbies": ["python", "games", "pizza"]}

user_id = users.insert_one(user1).inserted_id

#inserting multiple documents

users = [{"username": "third", "password": "12345"}, {"username": "red", "password": "blue"}]

Users = db.users

inserted = Users.insert_many(users)
inserted.inserted_ids 





