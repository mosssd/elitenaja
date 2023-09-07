import pymongo
from bson.objectid import ObjectId
import pprint
from id_generator import *

printer = pprint.PrettyPrinter()

connection_string = "mongodb+srv://radnha:radnha2435@softenproject-database.ochwdfb.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_string)

WorksCollection = client["NineTest"]["Works"]
RecruitersCollection = client["NineTest"]["Recruiters"]


def job_cost_calculator(number_requirement, hourly_income, start_time, end_time):
    start_time = start_time.split(":")
    end_time = end_time.split(":")
    start_f = float(start_time[0] + "." + start_time[1])
    end_f = float(end_time[0] + "." + end_time[1])
    hour_diff = end_f - start_f
    return number_requirement * hourly_income * hour_diff
    

def return_list_items(cursor, name_header):
    res = []
    for item in cursor:
        item["_id"] = str(item["_id"])
        res.append(item)
    return {name_header: res}


def return_items(item, name_header):
    item["_id"] = str(item["_id"])
    return {name_header: item}

def insertPseudoWork(work, recruiter_id):
    work_id = gen_id()
    work["work_id"] = work_id
    work["recruiter_id"] = recruiter_id
    
    recruiter_credit = RecruitersCollection.find_one({"recruiter_id": recruiter_id})["credit"]
    
    job_cost = job_cost_calculator(work["number_requirement"], work["hourly_income"], work["start_time"], work["end_time"])
    if recruiter_credit < job_cost:
        return "your credit is too low just go to topup"

    RecruitersCollection.update_one({"recruiter_id": recruiter_id}, {"$inc": {"credit": -job_cost}})
    work["pot"] =  job_cost
    work["recruiter_id"] = recruiter_id
    WorksCollection.insert_one(work)
    RecruitersCollection.update_one({"recruiter_id": recruiter_id}, {"$addToSet": {"list_of_work": work_id}})
    # NotiToUser()
    return "you have created work"


def getWorkByWorkDate(work_date):
    work_list = WorksCollection.find({"work_day": work_date})
    return return_list_items(work_list, "work_list")



def getWorkByWorkID(work_id):
    item = WorksCollection.find_one({"work_id": work_id})
    return return_items(item, "work")
