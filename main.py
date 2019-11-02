import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://testpy:dY1HmsPgC74O4L1Q@gcpcluster-xvgjc.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]


# Insert one document to the DB
#post = {
#    "name":"kay",
#    "score":8
#    }
#collection.insert_one(post)

#Insert many documents in the DB
#post1 = {
#    "name":"Hector",
#    "score":23
#}
#post2 = {
#    "name":"Euclides",
#    "score":43
#}
#collection.insert_many([post1,post2])

# Find documents in the DB
#name = input('Insert the name to find in the DB: ')
#results = collection.find({"name":name})

#for result in results:
#    print("Name: "+result["name"])
#    print("Score: "+str(result["score"]))

# Find only one documet in the DB
#results = collection.find_one({"_id":0})
#print(results)

# All documents  in the DB
#results = collection.find({})
#for result in results:
#    print(result)

# Deleting one document in the DB
#post = {
#    "_id":3,
#    "name":"kay",
#    "score":8
#    }
#collection.insert_one(post)
#result = collection.delete_one({"_id":3})