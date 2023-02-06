import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("key.json")
defult_app = firebase_admin.initialize_app(cred,  {
	'databaseURL': "https://task-managerchat-bot-default-rtdb.firebaseio.com/"
})

ref = db.reference('/')
if not ref.get():
    ref.set({"Tasks":[]})

ref = db.reference('/Tasks')

def addTasks(tasks):
    tasks = tasks.split(',')
    for task in tasks:
        if task:
            ref.push().set({"task" :task.strip(), "done":False})
    return "Done"

def showData():
    data = ref.get()
    result = "Your Tasks are:\n"
    i = 1
    if not data:
        return "No Tasks available!!"
    done = {}
    notDone = {}
    for val in data.values():
        if val["done"]:
            done[i] = val["task"]
        else:
            notDone[i] = val["task"]
        i += 1
    
    result += "\nRemaining:\n"
    for key, val  in notDone.items():
        result += str(key) + " " + val + '\n'
    result += "\nCompleted:\n"
    for key, val  in done.items():
        result += str(key) + " " + val + '\n'
    return result

def DeleteData(number):
    number -= 1
    data = ref.get()
    for key, val in data.items():
        if not number:
            ref.child(key).set({})
            return "Done"
        number -= 1
    return "Select correct task number"

def MarkTask(num):
    num = num - 1
    data = ref.get()
    for key,val in data.items():
        if not num:
            ref.child(key).update({"done":True})
            return "Done"
        num -= 1
    return "Select correct task number"

def QueryResponse(query):
    if not query:
        return 
    query = query.strip(" ")
    command = query.split(' ', 1)
    # adding task in the db.
    if command[0].lower() == 'add':
        if len(command) > 1:
            return addTasks(command[1])
        else:
            return "To add task Write Command:\nADD <task> or <task1>, <task2>" 
    
    elif command[0].lower() == "show":
        return showData()
    
    elif command[0].lower() == 'delete':
        if len(command) > 1:
            return DeleteData(int(command[1]))
        else:
            return showData() + "\nTo delete write:\nDELETE <NUMBER ASSOCIATED WITH TASK>"
    
    elif command[0].lower() == "mark":
        if len(command) > 1:
            return MarkTask(int(command[1]))
        else:
            return showData() + "\nTo mark task done write:\nMARK <NUMBER ASSOCIATED WITH TASK>"
    elif command[0].lower() == "help":
        return '''
        These are the instructions to preform Oparations:

        To ADD task write:
        ADD <task> or <task1>, <task2>

        To See all the tasks Write:
        SHOW

        To Delete the task write:
        DELETE <NUMBER ASSOCIATED WITH TASK>

        To Mark  the task as done write:
        MARK <NUMBER ASSOCIATED WITH TASK>
        '''

    else:
        return "Hey, I am a Task Manager\nCommnds:\nADD\nSHOW\nMARK DONE\nDELETE"