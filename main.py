import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://<username>:<password>@gcpcluster-xvgjc.gcp.mongodb.net/test?retryWrites=true&w=majority")