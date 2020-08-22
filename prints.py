import time
import os
from termcolor import colored, cprint
clearString = None

if os.name == 'nt':
    clearString = 'cls'
else:
    clearString = 'clear'


def newton(_time, _text, _color):
    counter = 0
    while counter < float(_time)/0.2:
        os.system(clearString)
        if counter % 4 == 0:
            print("╔════╤╤╤╤════╗")
            print("║    │││ \\   ║")
            print("║    │││  O  ║")
            print("║    OOO     ║")
            print(colored(_text, _color))
        elif counter % 4 == 1:
            print("╔════╤╤╤╤════╗")
            print("║    ││││    ║")
            print("║    ││││    ║")
            print("║    OOOO    ║")
            print(colored(_text+'.', _color))
        elif counter % 4 == 2:
            print("╔════╤╤╤╤════╗")
            print("║   / │││    ║")
            print("║  O  │││    ║")
            print("║     OOO    ║")
            print(colored(_text+'..', _color))
        elif counter % 4 == 3:
            print("╔════╤╤╤╤════╗")
            print("║    ││││    ║")
            print("║    ││││    ║")
            print("║    OOOO    ║")
            print(colored(_text+'...', _color))
        counter += 1
        time.sleep(0.2)
    os.system(clearString)


def print_help(additionalWait):
    if additionalWait:
        time.sleep(0.5)
    print(colored('Commands:', 'cyan', attrs=['underline']))
    print(colored('"help" for get list of commands.', 'cyan'))
    print(colored('"add" for add new student.', 'cyan'))
    print(colored('"show" for show all students.', 'cyan'))
    print(colored('"showone" for show one student with ID.', 'cyan'))
    print(colored('"remove" for remove student with ID.', 'cyan'))
    print(colored('"update" for update student with ID.', 'cyan'))
    print(colored('"save" for save students to db.', 'cyan'))
    print(colored('"autosave" for turn on/off auto save.', 'cyan'))
    print(colored('"reload" for reload students from db.', 'cyan'))
    print(colored('"drop" for delete all students from db.', 'cyan'))
    print(colored('"clear" for clear screen.', 'cyan'))
    print(colored('"exit" for exit app.', 'cyan'))
