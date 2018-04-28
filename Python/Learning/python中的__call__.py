''' 改进一下前面定义的斐波那契数列：
class Fib(object):
    ???
请加一个__call__方法，让调用更简单：

>>> f = Fib()
>>> print f(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34] '''

class Fib(object):
    def __init__(self):
        pass

    def __call__(self, num):
        L = [0, 1]
        for i in range(num - 2):
            L.append(L[-1] + L[-2])
        return L

f = Fib()
print(f(10))