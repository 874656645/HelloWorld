# 在Python 3.x, 取消了 cmp 参数， 只保留了Key Function参数。

class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s, %d)' % (self.name, self.score)

    __repr__ = __str__

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]

print(sorted(L, key=lambda s: (-s.score, s.name)))