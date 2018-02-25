# 如果类属性是带有双下划线的，则不能在外部调用此属性，但是可以在类的内部使用

class Person(object):
    
    __count = 0

    def __init__(self, name):
        Person.__count += 1
        self.name = name
        print(Person.__count)

p1 = Person('Bob')
p2 = Person('Alice')

try:
    print(Person.__count)
except AttributeError as error:
    print('AttributeError: %s' % error)