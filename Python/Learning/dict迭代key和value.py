''' 请根据dict：
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
打印出 name : score，最后再打印出平均分 average : score。 '''

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}

d2 = {}

sum = 0.0
for k, v in d.items():
    d2[k] = v
    sum += v
    print('%s : %d'%(k, v))
print('average:', sum / len(d))

for k in d2:
    print('key = %s, value = %d' %(k, d2[k]))
