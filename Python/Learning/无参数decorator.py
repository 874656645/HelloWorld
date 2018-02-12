# 请编写一个@performance，它可以打印出函数调用的时间。

import time

def performance(f):
    def fn(*args, **kwargs):
        print("call %s() at %s" % (f.__name__, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        return f(*args, **kwargs)
    return fn

@performance
def factorial(n):
    from functools import reduce
    return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial(10))