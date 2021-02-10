dictionary = {
    "27014000":{
        "name": "Jose Armando Alfarez",
        "birth-date": "02/07/1998",
        'major':"Bachelor of science",
        "minor": "Systems Engineering"
    },
    "26809000":{
        "name":"Rodolfo Alejandro Hernandez",
        "birth-date": "27/05/1999",
        "major": "Bachelor of Science",
        "minor": "Electrical Engineering"
    },
    "230110000": {
        "name":"maria del carmen Guzman",
        "birth-date": "12/11/1995",
        "major": "Bachelor of arts",
        "minor": "Economic"
    }
}

students = []
#for cedula in dictionary:
#    students = dictionary.get(cedula)
#    print(students)

for key, value in dictionary.items():
    value['dni'] = key
    students.append(value)

for student in students:
    dni = student['dni']
    Name = student['name']
    birt_date = student['birth-date']
    major = student['major']
    minor = student['minor']
    print(dni, Name, major, minor, birt_date, sep="/")





