d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    # 'Paul': [75, 86, 100],
    ('a', 'b') : True
}
print(d)

# 遍历dict
for key in d:
    print('%s: %d'%(key, d[key]))

# 添加键值对或者更新已有键值对的value
print(d)
d['xxx'] = 90
print(d)

# 判断key是否在dict中
if 'xxx' in d:
    print(d['xxx'])
else:
    print('None')

if d.get('xxx') == None:
    print('not in dict')

# 计算dict的长度
print(len(d))
# 注意字符串和数字之间不能用+号，只能用，
# print('Adam' + ':', d['Adam'])
# print('Lisa' + ':', d['Lisa'])
# print('Bart' + ':', d['Bart'])
