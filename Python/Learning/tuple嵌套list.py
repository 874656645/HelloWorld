# tuple不可变是指tuple中的元素指向是不可变的
''' t = ('a', 'b', ['A', 'B'])
print(t)
t[2].append('C')
print(t)
t[2][0],t[2][1] = 'X', 'Y'
print(t) '''

t = ('a', 'b', ('A', 'B'))
print(t[2])