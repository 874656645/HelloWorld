class Person(object):
    
    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self, name):
        Person.__count += 1
        self.name = name

print(Person.how_many())

p1 = Person('Bob')

print(Person.how_many())