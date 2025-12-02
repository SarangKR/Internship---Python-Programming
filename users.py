import json
import hashlib

DATABASE_FILE = 'database.json'

def load_data():
    try:
        with open(DATABASE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"users": [], "auctions": []}


def save_data(data):
    with open(DATABASE_FILE, 'w') as f:
        json.dump(data, f)


def register_user(username, password):
    data = load_data()
    if any(user['username'] == username for user in data['users']):
        return "Username already exists."

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    data['users'].append({"username": username, "password": hashed_password})
    save_data(data)
    return "User registered successfully."


def login_user(username, password):
    data = load_data()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    for user in data['users']:
        if user['username'] == username and user['password'] == hashed_password:
            return "Login successful."
    return "Invalid username or password."
