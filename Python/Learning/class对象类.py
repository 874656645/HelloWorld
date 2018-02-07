class Person(object):

    hobby = 'Play Computer'          # 静态属性(类属型)

    def __init__(self, name, age, weight):
        self.name = name        # 公开属性
        self._age = age         # 私有属性
        self.__weight = weight  # 私有变量
    
    @classmethod                # 类方法，静态方法
    def get_hobby(cls):
        return cls.hobby

    @property                   # 可以像属性一样调用的方法，不用写括号
    def get_weight(self):
        return self.__weight
    
    def self_introduction(self):# 正常的对象方法    
        print('My name is %s.\nI am %s years old.\n' % (self.name, self._age))

# 继承
class Programer(Person):

    def __init__(self, name, age, weight, language):
        super(Programer, self).__init__(name, age, weight)      # super第一个参数是当前子类，不是父类
        self.language = language

    def self_introduction(self):        # 重写的函数
        print('My name is %s.\nMy favorate language is %s' % (self.name, self.language))

# 多态
def introduce(person):
    if isinstance(person, Person):
        person.self_introduction()

if __name__ == '__main__':
    zs = Programer('张三', 18, 90, 'Python')
    ls = Person('李四', 20, 100)

    introduce(zs)
    introduce(ls)
    # print(zs)
    # print(type(zs))
    # print(isinstance(zs, Person))
    # print(issubclass(Programer, Person))
    # print(dir(zs))
    # print(zs.__dict__)
    # print(Person.get_hobby())
    # print(zs.get_weight)
    # zs.self_introduction()