# higher order functions

grades = [45.0, 61.5, 70.0, 81.5, 31.5, 68.25, 73.0, 100.0]

def scaleAssignmentGrade(percent):
    return percent * 0.15

#scaledGrades = list(map(scaleAssignmentGrade, grades))
scaledGrades = list(map(lambda g: g * 0.15, grades))
print('Scaled grades:', scaledGrades)

from functools import reduce

def min2(a, b):
    if a < b:
        return a 
    else:
        return b

#minimum = reduce(min2, grades)
minimum = reduce(lambda a,b: a if a < b else b, grades)
print('Minimum grade:', minimum)

def isLong(name):
    if len(name) > 7:
        return True 
    else:
        return False 

names = ['Salvatore', 'Ralph', 'Sandy', 'Bartholomew', 'Harkirat']
#longNames = list(filter(isLong, names))
longNames = list(filter(lambda name: True if len(name) > 7 else False, names))
print('The long names are', longNames)

# debugging
print('-------------------------------')

# syntax error (compile time in compiled languages)
age = 17
if age < 18:  # remove the : for a syntax error
    print('You cannot vote!')

# runtime error
courseName = 'CSCI 1030U'
#print('The 31st letter in the string is', courseName[30])

numUs = 0
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    #print('   checking the character:', courseName[i])
    if courseName[i] == 'c' and courseName[i] == 'C':
        numUs += 1
print(courseName, 'has', numUs, 'U(s) in it.')
