''' 对于Person类的定义：

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

希望除了 name和gender 外，可以提供任意额外的关键字参数，并绑定到实例，请修改 Person 的 __init__()定 义，完成该功能。
 '''

class Person(object):
    def __init__(self, name, gender, **kwargs):
        self.name = name
        self.gender = gender
        for k,v in kwargs.items():
            setattr(self, k, v)

p = Person('Bob', 'Male', age = 30, course = 'English')

print(p.age)
print(p.course)
print(dir(Person))
print(dir(p))