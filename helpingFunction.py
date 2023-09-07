import datetime
from datetime import datetime, timedelta
import pprint

base_id = 0

def gen_id():
    global base_id
    base_id += 1
    return base_id

def reset_id():
    global base_id
    base_id = 0


def return_items(item, name_header):
    return {name_header: item}



def getNowDate():
    today = datetime.now()
    x = str(today).split(' ') 
    date_of_today = x[0].split('-')
    return date_of_today

def getNowTime():
    today = datetime.now()
    x = str(today).split(' ') 
    date_of_today = x[1].split('-')
    return date_of_today

def getNowDayName():
    today = datetime.now()
    day_name = today.strftime('%A')
    return day_name

def genNext12Days():
    date_of_today = getNowDate()
    start = datetime(int(date_of_today[0]), int(date_of_today[1]), int(date_of_today[2]))
    K = 13
    res = []
    for day in range(K):
        date = (start + timedelta(days = day)).isoformat()
        date = date.split('T')[0].split('-')
        qq = datetime(int(date[0]), int(date[1]), int(date[2]))
        ddate = str(date[0]) + '-' + str(date[1]) + '-' + str(date[2])
        day_name = qq.strftime('%A')
        temp = [ddate, day_name]
        res.append(temp)
    res = res[1:]
    return return_items(res, "next12Days")
        
        


