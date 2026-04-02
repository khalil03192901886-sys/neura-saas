users_db = {}

def create_user(username, password):
    users_db[username] = password
    return True

def verify_user(username, password):
    return users_db.get(username) == password
