students = {
    'name' : 'ahmad', 
    'address' :'jakarta',
    'age' : 10, 
    'active' : True,
    'subject': ['math,english']

}
print(students)
print(type(students))

print(students)
print(students.keys())
print(students['subject'])
print(students['age'])

students['grade'] = 5
print(students)

students.update({'phone': '0889','email' : 'ahmad@gmail.com'})
print(students)

students.pop('active')
print(students)

students.popitem()
print(students)

employee = dict(name = 'joko',address = 'bekasi')
print(employee)


cars = {
    'merk': 'honda',
    'color' : 'white',
    'year': 2000
}

print(cars)
print(type(cars))