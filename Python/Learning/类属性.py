''' 请给 Person 类添加一个类属性 count，每创建一个实例，count 属性就加 1，
这样就可以统计出一共创建了多少个 Person 的实例。 '''

class Person(object):
    count = 0
    address = 'Earth'

    def __init__(self, name):
        Person.count = Person.count + 1
        self.name = name

p1 = Person('Bob')
print(Person.count)
p2 = Person('Alx')
print(Person.count)

# 每次实例化实际上是把类属型进行了一次拷贝，所以如果修改一个实例的类属型不影响其他实例的类属型
print(p1.address)
print(p2.address)
p1.address = 'Mars'
print(p1.address)
print(p2.address)
