

base_id = 0

def gen_id():
    global base_id
    base_id += 1
    return base_id

def reset_id():
    global base_id
    base_id = 0