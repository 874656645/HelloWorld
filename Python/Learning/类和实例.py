# 请练习定义Person类，并创建出两个实例，打印实例，再比较两个实例是否相等。

class Person(object):
    def __init__(self, name):
        self.name = name

xiaoming = Person('小明')
xiaohong = Person('小红')

print(xiaoming)

print(xiaohong)

print(xiaoming == xiaohong)