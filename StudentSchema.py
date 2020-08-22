class Student:
    def __init__(self, _id, _name, _surname, _email, _phone):
        self.id = int(_id)
        self.name = _name
        self.surname = _surname
        self.email = _email
        self.phone = _phone

    def obj(self):
        return {"id": self.id, "name": self.name, "surname": self.surname, "email": self.email, "phone": self.phone}

    def show(self):
        return [str(self.id), self.name, self.surname, self.email, self.phone]


def is_email(email):
    flagAt = False
    atIndex = email.find('@')
    if atIndex > 0:
        flagAt = True

    flagDot = False
    dotIndex = email.find('.', atIndex)
    if dotIndex > 0:
        flagDot = True
    return flagAt and flagDot


def is_phone(phone):
    flag = True
    if not phone[0:4]=='+994':
        flag = False
    return flag


def createStudent(_id, _name, _surname, _email, _phone):
    errors = []
    if not _id.isnumeric():
        errors.append('ID should be integer.')
    if not len(_id) == 3:
        errors.append('ID should be consist of 3 numbers.')
    if not _name.isalpha():
        errors.append('Name should only consist letters.')
    if not _surname.isalpha():
        errors.append('Name should only consist letters.')
    if not is_email(_email):
        errors.append('Please enter valid e-mail address.')
    if not is_phone(_phone):
        errors.append('Please enter valid phone number.')
    student = None
    if len(errors) == 0:
        student = Student(_id, _name, _surname, _email, _phone)

    return [errors, student]
