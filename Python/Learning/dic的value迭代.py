''' 给定一个dict：
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

请计算所有同学的平均分。 '''

# 版本3没有itervalues()方法了
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
print(d.values())
print(sum(d.values()) / len(d))
# sum = 0.0
# for score in d.values():
#     sum += score
# print(sum / len(d))