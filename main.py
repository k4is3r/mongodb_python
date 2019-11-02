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
post1 = {
    "name":"Hector",
    "score":23
}
post2 = {
    "name":"Euclides",
    "score":43
}
collection.insert_many([post1,post2])