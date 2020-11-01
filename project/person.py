class Person:
    def __init__(self, firstname, lastname, height, weight, admission_no, DOB, gender,
                  address, phoneNumber, email, fathername, fatheroccupation, password):
        self.firstname = firstname
        self.lastname = lastname
        self.height = height
        self.weight = weight
        self.admission_no = admission_no
        self.DOB = DOB
        self.gender = gender

        self.address = address
        self.email = email
        self.phoneNumber = phoneNumber

        self.fathername = fathername
        self.fatheroccupation = fatheroccupation

        self.password = password

    def __repr__(self):
        return f'firstname : {self.firstname}\n' \
               f'lastname : {self.lastname}\n' \
               f'height : {self.height}\n' \
               f'weight : {self.weight}\n' \
               f'admission number : {self.admission_no}\n' \
               f'DOB : {self.DOB}\n' \
               f'gender : {self.gender}\n' \
               f'address : {self.address}\n' \
               f'email : {self.email}\n' \
               f'phone number : {self.phoneNumber}\n' \
               f'father name : {self.fathername}\n' \
               f'father occupation : {self.fatheroccupation}\n' \
               f'password : {self.password}'
