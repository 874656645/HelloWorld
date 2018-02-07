def average(*args):
    res = 0.0
    if len(args) > 0:
        res = sum(args) / len(args)
    return res

print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))