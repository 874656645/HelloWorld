class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Teacher(Person):
    def __init__(self, name, gender, course):
        # python 3中不必传入子类和实例变量了
        # super(Teacher, self).__init__(name, gender)
        super().__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
print(t.name)
print(t.course)