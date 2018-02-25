# 请给Person类的__init__方法中添加name和score参数，并把score绑定到__score属性上，看看外部是否能访问到。

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

try:
    print(p.name)
    print(p.__score)
except AttributeError as error:
    print('AttibuteError: %s' % (error))