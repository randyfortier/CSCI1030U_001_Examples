class Student:
    def __init__(self, first, last, sid, gpa):
        self.first_name = first 
        self.last_name = last 
        self.sid = sid 
        self.gpa = gpa 
        self.marks = [] # alt: {}
    
    def set_mark(self, course, mark):
        self.marks.append(mark) # alt: self.marks[course] = mark

    def get_average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum / len(self.marks)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.sid + ')'

carla = Student('Carla', 'Smith', '100000001', 4.0)
print(carla)

class PerfectSquares:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += 1
        return self.current ** 2

squares = PerfectSquares()
for value in squares:
    if value < 1000:
        print(value)
    else:
        break

class Iguana:
    def __init__(self, name, mass):
        self.name = name 
        self.mass = mass
    
    def __lt__(self, anotherIguana):
        return self.mass < anotherIguana.mass
        # this is equivalent to:
        #if self.mass < anotherIguana.mass:
        #    return True 
        #else:
        #    return False

gary = Iguana('Gary', 1.1)
luther = Iguana('Luther', 0.7)
#print(gary < luther)
if gary < luther:
    print('Gary is lighter')
else:
    print('Gary is heavier')
