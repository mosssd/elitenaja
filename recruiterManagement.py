import pymongo
from bson.objectid import ObjectId
import pprint
from datetime import datetime
from id_generator import *


connection_string = "mongodb+srv://radnha:radnha2435@softenproject-database.ochwdfb.mongodb.net/?retryWrites=true&w=majority"



# date and time now
today = datetime.now()
x = str(today).split(' ') 
dayName = today.strftime('%A')

client = pymongo.MongoClient(connection_string)
RecruitersCollection = client["NineTest"]["Recruiters"]



def insertPseudoRecruiter(recruiter):
    recruiter_id = gen_id()
    recruiter["recruiter_id"] = recruiter_id
    RecruitersCollection.insert_one(recruiter)
    

    
    






