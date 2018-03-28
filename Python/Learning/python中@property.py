''' 如果没有定义set方法，就不能对“属性”赋值，这时，就可以创建一个只读“属性”。

请给Student类加一个grade属性，根据 score 计算 A（>=80）、B、C（<60）。
 '''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        return 'A' if self.__score >=80 else 'B' if self.__score >= 60 else 'C'
    
s = Student('Bob', 59)
print(s.grade)

s.score = 600
print(s.grade)

s.score = 99
print(s.grade)