sum = 0
x = -1
while True:
    x += 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum += x
print(sum)