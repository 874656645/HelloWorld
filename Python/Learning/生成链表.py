''' 请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
提示：range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...] '''

L = [x ** 2 for x in range(1, 11)]
print(L)
L = [x * (x + 1) for x in range(1, 101, 2)]
print(L)