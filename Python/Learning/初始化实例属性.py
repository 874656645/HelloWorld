''' 请定义Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，
并把他们都作为属性赋值给实例。 '''

class Person(object):
    def __init__(self, name, gender, birth, **kwargs):
        self.name = name
        self.gender = gender
        self.birth = birth
        # 动态添加属性，其实就是在一个dic中添加key和value
        # self.__dic__
        for key,value in kwargs.items():
            setattr(self, key, value)

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print(xiaoming.name)
print(xiaoming.job)