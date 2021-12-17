import os
import pymongo

from mongo import DATABASE

if os.path.exists("env.py"):
    import env

MONGO_URL = os.environ.get("MONGO_URL")
DATABASE = "myFirstDatabase"
COLLECTION = "celebreties"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def add_record():
  print("")
  first = input("Enter first name > ")
  last = input("Enter last name > ")
  dob = input("Enter date of birth > ")
  gender = input("Enter gender > ")
  hair_color = input("Enter hair color > ")
  occupation = input("Enter occupation > ")
  nationality = input("Enter nationality > ")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("you have selected option 2")
        elif option == "3":
            print("you have selected option 3")
        elif option == "4":
            print("you have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URL)

coll = conn[DATABASE][COLLECTION]

main_loop()