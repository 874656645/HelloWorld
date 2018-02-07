''' range(1, 101)
[1, 2, 3, ..., 100]
请利用切片，取出：
1. 前10个数；
2. 3的倍数；
3. 不大于50的5的倍数。 '''

L = range(1, 101)
L1 = L[:10]
L2 = L[2::3]
L3 = L[4:50:5]
LT = []
for item in L1:
    LT.append(item)
print(LT)
LT.clear()
for item in L2:
    LT.append(item)
print(LT)
LT.clear()
for item in L3:
    LT.append(item)
print(LT)