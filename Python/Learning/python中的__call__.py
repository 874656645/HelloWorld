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