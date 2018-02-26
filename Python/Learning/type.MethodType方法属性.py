# 函数不需要和实例对象self绑定，方法必须要和self绑定
# 方法也可以认为是类的属性
import types

def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.fn_attr = lambda : 'This is an attribute.'

p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1)
# 实例方法
print(p1.__init__)
# 方法属性
print(p1.get_grade)
# 函数属性
print(p1.fn_attr)

print(p1.get_grade())
p2 = Person('Cindy', 90)
try:
    print(p2.get_grade)
except AttributeError as error:
    print(error)