import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://testpy:dY1HmsPgC74O4L1Q@gcpcluster-xvgjc.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

