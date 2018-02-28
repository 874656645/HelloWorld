''' 
比较运算符：__eq__, __ne__, __lt__, __gt__, __le__, __ge__
数字运算符：__add__, __sub__, __mul__, __div__
逻辑运算符：__or__, __and__ 
转换为字符串：__str__, __repr__, __unicode__
属性访问控制：__setattr__, __getattr__, __getattribute__, __delattr__
'''

class Person(object):

    # def __new__(cls, *args, **kwargs):
    #     print('call __new__ method')
    #     print(args)
    #     print(kwargs)
    #     return super(Person, cls).__new__(cls)          # 3.5+版本必须这么写 
   

    def __init__(self, name, age):
        # print('call __init__ method')
        self.name = name                    # 此处会调用类的setattr方法
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    # 重载加法运算符
    def __add__(self, other):
        if isinstance(other, Person):
            return self.age + other.age
        else:
            raise Exception('类型错误')

    # 重载等于运算符
    def __eq__(self, other):
        if isinstance(other, Person):
            return other.age == self.age
        else:
            raise Exception('类型错误')

    # 重载打印对象字符串函数 print
    def __str__(self):
        return '%s is %d years old.' % (self.name, self.age)

    # 重载列举对象属性函数 dir
    def __dir__(self):
        return self.__dict__.keys()

    # 设置属性，在构造函数设置属性时会调用此函数
    def __setattr__(self, name, value):
        # setattr(self, name, value)              # 这么写会造成递归调用
        self.__dict__[name] = value

    # 查询属性，在构造函数中初始化属性时会调用此函数
    def __getattribute__(self, name):
        # return getattr(name)
        # return self.__dict__[name]
        return super(Person, self).__getattribute__(name)

    # 查询属性，只有当全局函数getattr函数被调用时才会触发此函数
    def __getattr__(self, name):
        return self._dict__[name]



if __name__ == '__main__':

    # 在对象初始化的时候，在init函数中会调用setattr函数对属性赋值
    zs = Person('zs', 18)
    # print(zs.name)
    setattr(zs, 'name', 'ls')
    print(getattr(zs, 'name'))
    print(dir(zs))
    # print(zs.name)
    # ls = Person('ls', 30)
    # print(zs)
    # print(dir(zs))
    # o = object()
    # print(zs + ls)
    # print(zs == ls)
    # print(zs.__dict__)
    # print(dir(zs))
    # print(dir(o))