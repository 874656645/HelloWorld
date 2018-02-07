''' 利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。 '''

# 方法一：三层嵌套循环
print([100 * i + 10 * j + k for i in range(1,10) for j in range(0, 10) for k in range(0, 10) if i == k])
# 方法二：
print([x * 100 + y * 10 + x for x in range(1, 10) for y in range(10)])
# 方法三：转换为字符串
print([x for x in range(100, 1000) if str(x)[0] == str(x)[-1]])
# 方法四：字符串倒序
print([x for x in range(100, 1000) if str(x) == str(x)[::-1]])