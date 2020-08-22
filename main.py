import json
from random import randint
import os
import time
from StudentSchema import Student, createStudent
from prettytable import PrettyTable
from pyfiglet import Figlet
from termcolor import colored, cprint
from prints import newton, print_help

# Dataları saxlayacaq faylın adı
dbFileName = "data.json"

# Daha professional görünməsi üçün gözləmə zamanı:)
additionalWait = False

# terminalı təmizləmək üçün əmr.Linux da clear, Windowsda cls
clearString = None

if os.name == 'nt':
    clearString = 'cls'
else:
    clearString = 'clear'

# terminalı təmizlə
os.system(clearString)


# şagird siyahısı
studentList = []

# Hər dəyişiklikdən sonra save et?
autosave = False


def read_json_db():
    # Əgər fayl yaradılmayıbsa boş bir arraydan ibarət json faylı yarat
    if not os.path.isfile('./'+dbFileName):
        print(colored('DB file missing...', 'red'))
        jsonFileCreate = open(dbFileName, 'xt')
        print(colored('...Created db.json file...', 'cyan'))
        jsonFileWrite = open(dbFileName, 'wt')
        jsonFileWrite.write('[]')
        jsonFileWrite.close()
        if additionalWait:
            newton(2, 'Fixing', 'cyan')
        print(colored('...DB is ready', 'green'))
    # Fayl varsa içindəki json array-a çevirib sonra içindəki obyektləri Student obyektinə çevir
    else:
        jsonFileRead = open(dbFileName, 'rt')
        jsonArray = json.loads(jsonFileRead.read())
        for i in jsonArray:
            studentList.append(
                Student(i["id"], i["name"], i["surname"], i["email"], i["phone"]))
        if additionalWait:
            newton(2, 'Loading', 'cyan')
        print(colored('Loaded data successfully!!!', 'green'))


# JSON faylındakı məlumatların oxunması
read_json_db()

# başlıq
print(Figlet(font="slant").renderText('Student\nManager'))

print_help(additionalWait)


def save_to_db(prefix=''):
    # Əgər fayl yaradılmayıbsa boş bir arraydan ibarət json faylı yarat
    if not os.path.isfile('./'+dbFileName):
        print(colored('DB file missing...', 'red'))
        jsonFileCreate = open(dbFileName, 'xt')
        print(colored('...Created db.json file...', 'cyan'))
        jsonFileWrite = open(dbFileName, 'wt')
        jsonFileWrite.write('[]')
        jsonFileWrite.close()
        if additionalWait:
            newton(2, 'Fixing', 'cyan')
        print(colored('...DB is ready', 'green'))
    # studentList də olan obyektləri dict-ə çevirib JSON a yaz
    else:
        jsonFileWrite = open(dbFileName, 'wt')
        jsonList = []
        for i in studentList:
            jsonList.append(i.obj())
        jsonFileWrite.write(json.dumps(jsonList))
        jsonFileWrite.close()
        if additionalWait:
            newton(1, 'Saving', 'cyan')
        print(colored(prefix+'Saved data successfully!!!', 'green'))


while True:
    command = input('(StudentManager)>> ')
    # help
    elif command == 'help':
        print_help(additionalWait)

    # add
    if command == 'add':
        print(colored('INFO: All fields are required', 'cyan'))
        id_code = None
        while not id_code:
            id_code = input('ID: ')
            if id_code:
                break
        name = None
        while not name:
            name = input('Name: ')
            if name:
                break
        surname = None
        while not surname:
            surname = input('Surname: ')
            if surname:
                break
        email = None
        while not email:
            email = input('Email: ')
            if email:
                break
        phone = None
        while not phone:
            phone = input('Phone: ')
            if phone:
                break
        x = createStudent(id_code, name, surname, email, phone)
        if additionalWait:
            newton(5, 'Creating Student', 'cyan')
        if len(x[0]) > 0:
            for i in x[0]:
                print(colored(i, 'red'))
            print(colored('Cannot create student!', 'red'))
        else:
            studentList.append(x[1])
            print(colored('Created student successfully.', 'green'))
            if autosave:
                save_to_db('Autosave: ')

    # show
    elif command == 'show':
        table = PrettyTable()
        table.field_names = ['ID', 'Name', 'Surname', 'Email', 'Phone']
        if additionalWait:
            newton(3, 'Fetching', 'cyan')
        for i in studentList:
            table.add_row(i.show())
        print(table)
        if autosave:
            save_to_db('Autosave: ')

    # showone
    elif command == 'showone':
        _id = input('Enter ID: ')
        table = PrettyTable()
        table.field_names = ['ID', 'Name', 'Surname', 'Email', 'Phone']
        if additionalWait:
            newton(1, 'Fetching', 'cyan')
        for i in studentList:
            if i.id == int(_id):
                table.add_row(i.show())
        print(table)
        if autosave:
            save_to_db('Autosave: ')

    # remove
    elif command == 'remove':
        _id = input('Enter ID: ')
        if _id.isnumeric():
            found = False
            if additionalWait:
                newton(1, 'Removing', 'cyan')
            for st in studentList:
                if st.id == int(_id):
                    studentList.remove(st)
                    print(colored('Student deleted.', 'green'))
                    found = True
                    break
            if not found:
                print(colored('Cannot find student.', 'red'))
        else:
            print(colored('ID should be integer.', 'red'))
        if autosave:
            save_to_db('Autosave: ')

    # update
    elif command[0:6] == 'update':
        _id = command.split(' ')[1]
        cmdArr = command.split(' ')[2:]
        update_object = {}
        if _id.isnumeric():
            for i in studentList:
                if i.id == int(_id):
                    for key in cmdArr:
                        update_object[key] = input(
                            key.capitalize()+" ("+i.obj()[key]+"): ")
                    i.update(update_object)
        else:
            print(colored('ID should be integer', 'red'))
    
    # save
    elif command == 'save':
        save_to_db()

    # autosave
    elif command == 'autosave':
        if autosave:
            autosave = False
            print(colored('Turned off autosave.', 'cyan'))
        else:
            autosave = True
            print(colored('Turned on autosave.', 'cyan'))

    # reload
    elif command == 'reload':
        studentList = []
        read_json_db()

    # drop
    elif command == 'drop':
        jsonFileWrite = open(dbFileName, 'wt')
        jsonFileWrite.write('[]')
        if additionalWait:
            newton(1, 'Dropping', 'cyan')
        jsonFileWrite.close()

    # clear
    elif command == 'clear':
        os.system(clearString)

    # exit
    elif command == 'exit':
        break

    # TEST ÜÇÜN newton
    elif command[0:6] == 'newton':
        cmdArr = command.split(' ')
        newton(cmdArr[1], cmdArr[2], cmdArr[3])

    # command yoxdursa
    else:
        if len(command) > 0:
            print(colored('Cannot find command!', 'red'))
