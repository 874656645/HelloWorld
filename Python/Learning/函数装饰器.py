def f1(x):
    return x * 2

def new_fn(f):
    def fn(x):
        print('call', f.__name__ + '()')
        return f(x)
    return fn

print(f1(2))
# f1 = new_fn(f1)
# print(f1(2))