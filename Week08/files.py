sids = ['100000001', '100000002', '100000003', '100000004']
midtermMarks = [52.0, 71.5, 90.0, 44.25]

with open('midterm_grades.csv', 'w') as file:
    for i in range(len(sids)):
        file.write(sids[i] + ',' + str(midtermMarks[i]) + '\n')

'''
100000001, 52.0
100000002, 71.5
'''

import json
with open('students.json', 'r') as file:
    studentList = json.load(file)
    carla = studentList[0]
    print('Grades for', carla['firstName'], carla['lastName'])
    for grade in carla['grades']:
        print(grade * 0.5)

try:
    result = 3 / 0
    #print(midtermMarks[4]) # also generates an exception
except IndexError as e:
    print('IndexError:', e) 
except ZeroDivisionError as e:
    print('Cannot divide by zero')

class YouAreTooYoungError(Exception):
    pass

def buyBeer(age):
    if age < 19:
        raise YouAreTooYoungError('Wait until you are 19')
    print('Here is your beer madam/sir!')

try:
    buyBeer(20)
except YouAreTooYoungError as error:
    print('Sorry, but you cannot buy beer yet!')

for n in [5,4,3,2,1,0]:
    try:
        print(1/n)
    except ZeroDivisionError as error:
        print('infinity')

print('I caught all them exceptions!')