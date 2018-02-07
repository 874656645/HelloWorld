''' 请用for循环迭代数列 1-100 并打印出7的倍数。 '''

# 方法一：
# for i in range(1, 101):
#     if i % 7 == 0:
#         print(i)

# 方法二：
# 这种方式循环次数更少，扩大范围
# for i in range(1, 101):
#     t = i * 7
#     if t > 100:
#         break
#     print(t)

# 方法三：
# for i in range(0, 101, 7):
#     if i > 0:
#         print(i)