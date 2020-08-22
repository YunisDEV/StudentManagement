import json
from random import randint
import os
import time
from StudentSchema import Student, createStudent
from prettytable import PrettyTable
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
    print('Commands:')
    print('"help" for get list of commands.')
    print('"add" for add new student.')
    print('"show" for show all students.')
    print('"showone" for show one student with ID.')
    print('"remove" for remove student with ID.')
    print('"save" for save students to db.')
    print('"autosave" for turn on/off auto save.')
    print('"reload" for reload students from db.')
    print('"clear" for clear screen.')
    print('"exit" for exit app.')


os.system(clearString)
print('===============Studentify===============')

studentList = []
autosave = False


def read_json_db():
    jsonFileRead = open('db.json', 'rt')
    jsonArray = json.loads(jsonFileRead.read())
    for i in jsonArray:
        studentList.append(
            Student(i["id"], i["name"], i["surname"], i["email"], i["phone"]))
    print('Loaded data successfully!!!')


read_json_db()

print_help()


def save_to_db(prefix=''):
    jsonFileWrite = open('db.json', 'wt')
    jsonList = []
    for i in studentList:
        jsonList.append(i.obj())
    jsonFileWrite.write(json.dumps(jsonList))
    print(prefix+'Saved data successfully!!!')


while True:
    command = input('(Studentify)>> ')
    if command == 'add':
        id_code = input('ID: ')
        name = input('Name: ')
        surname = input('Surname: ')
        email = input('Email: ')
        phone = input('Phone: ')
        x = createStudent(id_code, name, surname, email, phone)
        if len(x[0]) > 0:
            for i in x[0]:
                print(i)
            print('Cannot create student')
        else:
            studentList.append(x[1])
            print('Created student successfully')
        if autosave:
            save_to_db('Autosave: ')
    elif command == 'newton':
        newton_toy()
    elif command == 'showone':
        _id = input('Enter ID: ')
        table = PrettyTable()
        table.field_names = ['ID', 'Name', 'Surname', 'Email', 'Phone']
        for i in studentList:
            if i.id==int(_id):
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
        for i in _id:
            if not i.isalnum():
                raise Exception('ID should be integer')
        found = False
        for st in studentList:
            if st.id == int(_id):
                studentList.remove(st)
                print('Student deleted.')
                found = True
                break
        if not found:
            print('Cannot find student.')
        if autosave:
            save_to_db('Autosave: ')
    elif command == 'save':
        save_to_db()
    elif command == 'reload':
        studentList = []
        read_json_db()
    elif command == 'help':
        print_help()
    elif command == 'clear':
        os.system(clearString)
    elif command == 'autosave':
        if autosave:
            autosave = False
            print('Turned off autosave')
        else:
            autosave = True
            print('Turned on autosave')
    elif command == 'exit':
        break
    else:
        if len(command) > 0:
            print('Cannot find command.')
