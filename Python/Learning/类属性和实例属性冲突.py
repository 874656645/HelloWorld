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

# 如果实例的属性名与类属性名相同，则会覆盖类属性名
print(p1.address)
print(p2.address)
p1.address = 'Mars'
print(p1.address)
print(p2.address)
# 删除实例的属性后，才能访问到类属性
del p1.address
print(p1.address)
print(p2.address)

