L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 求和函数, sum()
sum = sum(L)
print(sum)

# 求容器个数函数, len()
print(len(L))

# 链表函数, range(1, 101, 5)
L = range(0, 9)
print(tuple(L))

# 绝对值函数, abs()
x = -30
print(abs(x))

# 比较函数，在python3中没有cmp函数了
print('ac' < 'ab')
import operator
print(operator.lt(12, 21))

# 转换函数，8进制
x = int('123', 8)
print(str(x))

# 链表绑定索引函数，enumerate()
L = ['A', 'B', 'C']
for index, item in enumerate(L):
    print('%d-%s'%(index, item))

# 合并两个链表函数, zip()
L2 = ['A', 'B', 'C']
L1 = range(1, len(L2) + 1)
for index, item in zip(L1, L2):
    print('%d-%s'%(index, item))

# 判断变量类型
x = '101'
print(isinstance(x, str))
print(type(x) == str)

# 字符串倒序
s = 'abcdefg'
print(s[::-1])

# 列举对象属性和方法
class Person(object):
    # 类属型，所有实例共享
    name = 'a'

p = Person()
print(dir(p))

# 设置对象属性
print(Person.name)
# setattr(p, 'name', 'zs')          此处如果实例添加了与类同名的属性，则实例的属性会覆盖类的属性，最好不要添加与类属性同名的属性
p.name = 'zs'                       # 这一句也可以对实例添加属性，与上一句代码的效果相同，但是其他的实例并不会添加此属性
print(Person.name)
print(p.name)
del(p.name)
print(p.name)

p.age = 19
pp = Person()
print(pp.age)
# 无法对object实例添加属性
# o = object()
# o.age = 20
print(p.age)

# 查询对象属性
print(getattr(p, 'name'))

