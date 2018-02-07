''' Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：
输入：[2, 4, 5, 7, 12]
输出：2*4*5*7*12的结果 '''

def prod(x, y):
    return x * y
# 3.1版本后需要从functools中导入reduce模块
from functools import reduce
print(reduce(prod, [2, 4, 5, 7, 12]))
