''' 在第7节中，我们在sorted这个高阶函数中传入自定义排序函数就可以实现忽略大小写排序。
请用functools.partial把这个复杂调用变成一个简单的函数：
sorted_ignore_case(iterable) '''

import functools

sorted_ignore_case = functools.partial(sorted, key = lambda str:str[0].upper())

print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))

print(sorted)

print(sorted_ignore_case)
