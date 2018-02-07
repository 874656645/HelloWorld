def square_of_sum(L):
    sum = 0
    for item in L:
        sum += item ** 2
    return sum
        
print(square_of_sum([1, 2, 3, 4, 5]))
print(square_of_sum([-5, 0, 5, 15, 25]))