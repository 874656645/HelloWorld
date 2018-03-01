
class Person(object):
    
    def __init__(self, name, gender):
        super().__init__()
        self.name = name
        self.gender = gender

class Student(Person):
    
    def __init__(self, name, gender, score):
        super().__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(student: %s, %s, %d)' % (self.name, self.gender, self.score)
        # return ('student:', self.name, self.gender, self.score).__str__()

    __repr__ = __str__

s = Student('Bob', 'male', 90)

print(s)

print(dir(s))