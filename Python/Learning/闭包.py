# 返回闭包不能引用循环变量，请改写count()函数，让它正确返回能计算1x1、2x2、3x3的函数
''' 函数只在执行时才去获取外层参数i，若函数定义时可以获取到i，问题便可解决。
而默认参数正好可以完成定义时获取i值且运行函数时无需参数输入的功能，
所以在函数f()定义中改为f(m = i),函数f返回值改为m*m即可. '''

def count():
    fs = []
    for i in range(1, 4):
        def f(m = i):
            return m * m
        fs.append(f)
    return fs

f1, f2, f3 = count()

print('%d\n%d\n%d' % (f1(), f2(), f3()))