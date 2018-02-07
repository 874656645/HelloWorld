L = []
x = 1
while x < 10:
    L.append(x ** 3)
    x += 1
print(L)

L = []
x = 1
''' while x < 101:
    L.append(x ** 2)
    x += 1 '''
for num in range(1, 101):
    L.append(num ** 2)
print(sum(L))