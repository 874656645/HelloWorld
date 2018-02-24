''' 请思考带参数的@decorator，@functools.wraps应该放置在哪：
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            ???
        return wrapper
    return perf_decorator '''

import time
from functools import reduce
from functools import wraps
# 直接导入functools的话，在使用其内部函数时需要添加functools的模块名
# import functools

def performance(unit):
    def perf_decorator(f):
        @wraps(f)
        # @functools.wraps(f)
        def wrapper(*args, **kwargs):
            t1 = time.time()
            r = f(*args, **kwargs)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s in %d %s' % (f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def func(n):
    return reduce(lambda x,y : x*y, range(1, n+1))
    # return functools.reduce(lambda x,y : x*y, range(1, n+1))

print(func(20))
print(func.__name__)
