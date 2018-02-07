''' 一元二次方程的定义是：ax² + bx + c = 0

请编写一个函数，返回一元二次方程的两个解。

注意：Python的math包提供了sqrt()函数用于计算平方根 '''

import math

def quadratic_equation(a, b, c):
    dt = math.sqrt(b ** 2 - 4 * a * c)
    x1 = (-b + dt) / 2 / a
    x2 = (-b - dt) / 2 / a
    return x1,x2

print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))
    
