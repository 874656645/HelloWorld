''' 斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。

请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10) 可以打印出数列的前 10 个元素，len(Fib(10))可以正确返回数列的个数10。 '''

class Fib(object):
    
    def __init__(self, num):
        super().__init__()
        # 方法一：
        # self.__result = []
        # for i in range(0, num):
        #     if i == 0:
        #         self.__result.append(0)
        #     elif i == 1:
        #         self.__result.append(1)
        #     else:
        #         self.__result.append(self.__result[i - 1] + self.__result[i - 2])

        # 方法二：
        # a, b, L = 0, 1, []
        # for i in range(num):
        #     L.append(a)
        #     a, b = b, a+b
        # self.__result = L

        # 方法三：
        L = [0, 1]
        for i in range(num - 2):
            L.append(L[-1] + L[-2])
        self.__result = L
    
    def __str__(self):
        return str(self.__result)

    __repr__ = __str__

    def __len__(self):
        return len(self.__result)

f = Fib(10)

print(f)
print(len(f))
            