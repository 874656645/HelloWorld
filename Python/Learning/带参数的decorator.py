import time

def performance(unit):
    def per_decorator(f):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            r = f(*args, **kwargs)
            t2 = time.time()
            ''' t = 0
            if unit == 'ms':
                t = (t2 - t1) * 1000  
            else:
                t = (t2 - t1) '''
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f %s' %(f.__name__, t, unit))
            return r
        return wrapper
    return per_decorator

@performance('ms')
def factorial(n):
    from functools import reduce
    return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial(10))