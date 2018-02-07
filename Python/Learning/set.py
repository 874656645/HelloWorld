# 遍历set集合
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print('%s: %d'%(x[0], x[1]))

# 修改set集合
s= set(['Adam', 'Lisa', 'Paul'])
print(s)
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print(s)
