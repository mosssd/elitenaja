import pymongo
from bson.objectid import ObjectId
import pprint
from helpingFunction import *



connection_string = "mongodb+srv://radnha:radnha2435@softenproject-database.ochwdfb.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_string)

UsersCollection = client["NineTest"]["Users"]

def insertPseudoUser(user):
    user_id = gen_id()
    user["user_id"] = user_id
    UsersCollection.insert_one(user)
    

def addWorkToListOfWork(work_id, user_id):
    UsersCollection.update_one({"user_id": user_id}, {"$addToSet": {"list_of_work": work_id}})



