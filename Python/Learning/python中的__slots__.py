''' 假设Person类通过__slots__定义了name和gender，请在派生类Student中
通过__slots__继续添加score的定义，使Student类可以实现name、gender和score 3个属性。 '''

class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    __slots__ = ('score',)

    def __init__(self, name, gender, score):
        super().__init__(name, gender)
        self.score = score

s = Student('Bob', 'Male', 99)

print(s.score)