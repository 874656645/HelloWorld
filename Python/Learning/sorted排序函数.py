''' 原理：先比较元组的第一个值，FALSE<TRUE，如果相等就比较元组的下一个值，以此类推。

先看一下Boolean value 的排序：

print(sorted([True,Flase]))===>结果[False,True]

Boolean 的排序会将 False 排在前，True排在后 .  '''

''' 对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。

输入：['bob', 'about', 'Zoo', 'Credit']
输出：['about', 'bob', 'Credit', 'Zoo'] '''

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = lambda item:(item.upper())))

''' 一道面试题：

list1=[7, -8, 5, 4, 0, -2, -5]
#要求1.正数在前负数在后 2.整数从小到大 3.负数从大到小

sorted(list1,key=lambda x:(x<0,abs(x)))

解题思路：先按照正负排先后，再按照大小排先后。 '''

list1 = [7, -8, 5, 4, 0, -2, -5]
print(sorted(list1, key = lambda item:(item < 0, abs(item)), reverse=True))
# print(sorted(list1, key = lambda item:(item < 0, item > 0 and item, item < 0 and -item)))


''' 例1：

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave','B', 10)]

sorted(students,key=lambda s: x[2]) #按照年龄来排序

结果：[('dave','B', 10), ('jane', 'B', 12), ('john', 'A', 15)] '''

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave','B', 10)]
print(sorted(students, key=lambda s:(s[2])))

''' 例2.这是一个字符串排序，排序规则：小写<大写<奇数<偶数
s = 'asdf234GDSdsf23'  #排序:小写-大写-奇数-偶数

print("".join(sorted(s, key=lambda x: (x.isdigit(),x.isdigit() and int(x) % 2 == 0,x.isupper(),x))))'''
s = 'asdf234GDSdsf23'  #排序:小写-大写-奇数-偶数
print(''.join(sorted(s, key=lambda x:(x.isdigit(), x.isupper(), x.isdigit() and int(x) % 2 == 0, x))))