import models as db
from passlib.apps import custom_app_context as pwd_context
import getpass

def hash_password(password):
        return pwd_context.encrypt(password)
def validate_station(station_id):
        try:
            station_id = int(station_id)
            return True
        except ValueError:
            return False
def validate_username(username):
        return isinstance(username, str)
username = raw_input("Username: ")
while (not validate_username(username)):
    username = raw_input("Username can only be characters, input username: ")

password = getpass.getpass("Password: ")
hashed_password = hash_password(password)

station_id = raw_input("Station id: ")
while (not validate_station(station_id)):
    station_id = raw_input("Station id can only be integer, input station id: ")

db.insertUser(username, hashed_password, station_id)
