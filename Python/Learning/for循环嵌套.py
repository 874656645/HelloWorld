# 方法一：嵌套循环72次，更快速
for x in range(1, 10): # [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in range(2, 10): # [2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print(x * 10 + y)

# 方法二：循环90次，并且除法和取余操作浪费时间
''' x = 9 
while x < 100:
    x += 1
    m = x / 10
    n = x % 10
    if m < n:
        print(x) '''
print('End')