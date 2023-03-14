#installing simplejson package in bash with the command 'pip3 install simplejson'

import simplejson as json
import os

#if there is a file then read from the file otherwise create the file

#check if the file exists and if does exists then make sure it is an empty file
if os.path.isfile("./ages.json") and os.stat("./ages.json") != 0:
    old_file = open("./ages.json", "r+") #read and write the file if it does exists
    data = json.loads(old_file.read()) #reads the file and loads it to python and assign it to the data variable
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1
    print("new age is", data["age"])
else:
    old_file = open("./ages.json", "w+") #writing if the file does not exists
    data = {"name": "Nick", "age":27}
    print("No file found, setting default age to", data["age"])

#if there is a file then we are to write at position 0 otherwise it will append to the file
old_file.seek(0)
old_file.write(json.dumps(data))

