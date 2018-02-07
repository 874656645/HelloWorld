# 方法一：
t = (0, 1, 2, '3', 4, '5', 6, '7', 8, 9);

# 方法二：
# range(0,10) 表示list链表，加入tuple(range(0,10)), list链表则变成了 tuple不可改变的链表了
# t = tuple(range(0, 10));

# 方法三：
''' x = 0;
L = [];
while x < 10:
    L.append(x);
    x += 1;
t = tuple(L); '''

print(t);