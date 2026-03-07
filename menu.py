import os
import json
tasks = []
new_user = True

if not(os.path.exists("base.json")): #creates json base if not present
    with open("base.json","w")as f:
        f.write("[\n]")

def help():
    print("those are your commands")
    print(f"these are your tasks{tasks}")
    print("add")
    print("remove")
    print("quit")
    print("if you want to display this panel again write help")

def add():
    task = input()
    tasks.append(task)
    print("task added")
    base_py[user_id].update({"tasks":tasks}) #adding tasks to list in python
    with open("base.json","r+")as f:
        f.truncate(0)
        f.seek(0) #writing it into base.json file
        json.dump(base_py,fp=f,indent=4)
def remove():
    task = input()
    try:
        tasks.remove(task)
        with open("base.json","r+")as f:
            base_py[user_id].get("tasks").remove(task) #removes tasks from list in python
            f.truncate(0)
            f.seek(0) #writing changes in base.json file
            json.dump(base_py,fp=f,indent=4)
    except ValueError:
        print("remove valid task")

print("put your username")
username = input()
with open("base.json","r")as f:
    base_py = json.load(f) #getting base into python
    for i in base_py:
        if i["username"] == username: #checking if user is in base
            user_id = base_py.index(i) 
            print("welcome back")
            new_user = False 
            tasks = base_py[user_id].get("tasks") #getting tass from base
            
if new_user == True: #i am writing this in another if statment bc it got corrupted
        with open("base.json","r+")as f: 
            base_py.append({"username":username,"tasks":[]}) #adding user to list
            f.truncate(0)
            f.seek(0)
            json.dump(base_py,indent=4,fp=f) #writing user to base
            print("you have been added to userbase")
help()
while True:
    command = input("> ") #command line
    if command == "add":
        add()
    elif command == "remove":
        remove()
    elif command == "quit":
        break
    elif command == "help":
        help()
    else:
        print("wrong command")