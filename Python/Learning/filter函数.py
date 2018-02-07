''' 请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] '''

import math

def is_sqr(x):
    res = math.sqrt(x)
    return res == int(res)

print(list(filter(is_sqr, range(1, 101))))