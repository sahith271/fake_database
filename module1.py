from random import *
alphabets='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'
cities=['Hyderabad','Banglore','Mumbai', 'Delhi', 'Kolkata']
designations=['SDE', 'HR','Testing', 'Admin', 'Devops Engineer']

def emp_name():
    name=choice(alphabets).upper()
    for i in range(9):
        name=name+choice(alphabets)
    return name
def emp_no():
    emp_name='e-'
    for i in range(4):
        emp_name=emp_name+choice(numbers)
    return emp_name
def emp_salary():
    sal=uniform(10000,50000)
    return sal


def emp_city():
    city=choice(cities)
    return city


def emp_designation():
    designation=choice(designations)
    return designation
def emp_mob_num():
    number=choice('6789')
    for i in range(9):
        number=number+choice(numbers)
    return number

def emp_data():
    print('Employee Name', emp_name())
    print('Employee Number', emp_no())
    print('Employee Phone Number', emp_mob_num())
    print('Employee Designation', emp_designation())
    print('Employee City', emp_city())
    print('Employee salary {:.2f}'.format(emp_salary()))

for i in range(10):
    print(emp_data())



