# 请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。

def calc_prod(lst):
    def lazy_mul():
        from functools import reduce                # 一定要注意这句话
        return reduce((lambda x, y: x * y), lst)
    return lazy_mul

f = calc_prod([1, 2, 3, 4])

print(f())