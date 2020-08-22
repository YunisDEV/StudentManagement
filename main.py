import json
from random import randint
import os
import time
from StudentSchema import Student, createStudent
from prettytable import PrettyTable
from pyfiglet import Figlet
from termcolor import colored, cprint

dbFileName = "data.json"

clearString = None

if os.name == 'nt':
    clearString = 'cls'
else:
    clearString = 'clear'


def newton_toy():
    counter = 0
    while counter < 20:
        os.system(clearString)
        if counter % 4 == 0:
            print("╔════╤╤╤╤════╗")
            print("║    │││ \\   ║")
            print("║    │││  O  ║")
            print("║    OOO     ║")
        elif counter % 4 == 1:
            print("╔════╤╤╤╤════╗")
            print("║    ││││    ║")
            print("║    ││││    ║")
            print("║    OOOO    ║")
        elif counter % 4 == 2:
            print("╔════╤╤╤╤════╗")
            print("║   / │││    ║")
            print("║  O  │││    ║")
            print("║     OOO    ║")
        elif counter % 4 == 3:
            print("╔════╤╤╤╤════╗")
            print("║    ││││    ║")
            print("║    ││││    ║")
            print("║    OOOO    ║")
        counter += 1
        time.sleep(0.2)
    os.system(clearString)


def print_help():
    print(colored('Commands:', 'cyan', attrs=['underline']))
    print(colored('"help" for get list of commands.', 'cyan'))
    print(colored('"add" for add new student.', 'cyan'))
    print(colored('"show" for show all students.', 'cyan'))
    print(colored('"showone" for show one student with ID.', 'cyan'))
    print(colored('"remove" for remove student with ID.', 'cyan'))
    print(colored('"save" for save students to db.', 'cyan'))
    print(colored('"autosave" for turn on/off auto save.', 'cyan'))
    print(colored('"reload" for reload students from db.', 'cyan'))
    print(colored('"drop" for delete all students from db.', 'cyan'))
    print(colored('"clear" for clear screen.', 'cyan'))
    print(colored('"exit" for exit app.', 'cyan'))


os.system(clearString)

print(Figlet(font="slant").renderText('Student\nManager'))

studentList = []
autosave = False


def read_json_db():
    if not os.path.isfile('./'+dbFileName):
        print(colored('DB file missing...', 'red'))
        jsonFileCreate = open(dbFileName, 'xt')
        print(colored('...Created db.json file...', 'cyan'))
        jsonFileWrite = open(dbFileName, 'wt')
        jsonFileWrite.write('[]')
        print(colored('...DB is ready', 'green'))
    else:
        jsonFileRead = open(dbFileName, 'rt')
        jsonArray = json.loads(jsonFileRead.read())
        for i in jsonArray:
            studentList.append(
                Student(i["id"], i["name"], i["surname"], i["email"], i["phone"]))
        print(colored('Loaded data successfully!!!', 'green'))


read_json_db()

print_help()


def save_to_db(prefix=''):
    if not os.path.isfile('./'+dbFileName):
        print(colored('DB file missing...', 'red'))
        jsonFileCreate = open(dbFileName, 'xt')
        print(colored('...Created db.json file...', 'cyan'))
        jsonFileWrite = open(dbFileName, 'wt')
        jsonFileWrite.write('[]')
        print(colored('...DB is ready', 'green'))
    else:
        jsonFileWrite = open(dbFileName, 'wt')
        jsonList = []
        for i in studentList:
            jsonList.append(i.obj())
        jsonFileWrite.write(json.dumps(jsonList))
        print(colored(prefix+'Saved data successfully!!!', 'green'))


while True:
    command = input('(StudentManager)>> ')
    if command == 'add':
        print(colored('INFO: All fields are required','cyan'))
        id_code = None
        while not id_code:
            id_code = input('ID: ')
            if id_code: break
        name = None
        while not name:
            name = input('Name: ')
            if name: break
        surname = None
        while not surname:
            surname = input('Surname: ')
            if surname: break
        email = None
        while not email:
            email = input('Email: ')
            if email: break
        phone = None
        while not phone:
            phone = input('Phone: ')
            if phone: break
        x = createStudent(id_code, name, surname, email, phone)
        if len(x[0]) > 0:
            for i in x[0]:
                print(colored(i,'red'))
            print(colored('Cannot create student!', 'red'))
        else:
            studentList.append(x[1])
            print(colored('Created student successfully.', 'green'))
        if autosave:
            save_to_db('Autosave: ')
    elif command == 'newton':
        newton_toy()
    elif command == 'showone':
        _id = input('Enter ID: ')
        table = PrettyTable()
        table.field_names = ['ID', 'Name', 'Surname', 'Email', 'Phone']
        for i in studentList:
            if i.id == int(_id):
                table.add_row(i.show())
        print(table)
        if autosave:
            save_to_db('Autosave: ')
    elif command == 'show':
        table = PrettyTable()
        table.field_names = ['ID', 'Name', 'Surname', 'Email', 'Phone']
        for i in studentList:
            table.add_row(i.show())
        print(table)
        if autosave:
            save_to_db('Autosave: ')
    elif command == 'remove':
        _id = input('Enter ID: ')
        if _id.isnumeric():
            print(colored('ID should be integer.','red'))
            found = False
            for st in studentList:
                if st.id == int(_id):
                    studentList.remove(st)
                    print(colored('Student deleted.','green'))
                    found = True
                    break
            if not found:
                print(colored('Cannot find student.','red'))
        else:
            print(colored('ID should be integer.','red'))
        if autosave:
            save_to_db('Autosave: ')
    elif command == 'save':
        save_to_db()
    elif command == 'reload':
        studentList = []
        read_json_db()
    elif command == 'help':
        print_help()
    elif command == 'drop':
        jsonFileWrite = open(dbFileName, 'wt')
        jsonFileWrite.write('[]')
    elif command == 'clear':
        os.system(clearString)
    elif command == 'autosave':
        if autosave:
            autosave = False
            print(colored('Turned off autosave.','cyan'))
        else:
            autosave = True
            print(colored('Turned on autosave.','cyan'))
    elif command == 'exit':
        break
    else:
        if len(command) > 0:
            print(colored('Cannot find command!','red'))
