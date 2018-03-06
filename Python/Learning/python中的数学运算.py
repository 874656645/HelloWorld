''' Rational类虽然可以做加法，但无法做减法、乘方和除法，请继续完善Rational类，实现四则运算。

提示：
加法运算：__and__
减法运算：__sub__
乘法运算：__mul__
除法运算：__div__
 '''
def gcd(a, b):
    # 递归效率低
    ''' if b == 0:
        return a
    return gcd(b, a % b) '''
    while b:
        a,b = b,a%b
    return a


class Rational(object):
    def __init__(self, p, q):
        g = gcd(p,q)
        self.p = p / g
        self.q = q / g

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __truediv__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __int__(self):
        return int(self.p) // int(self.q)

    def __float__(self):
        return self.p / self.q

    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' %(self.p / g, self.q / g)

    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print (r1 + r2)
print (r1 - r2)
print (r1 * r2)
print (r1 / r2)
print(int(Rational(7, 2)))
print(float(Rational(1, 3)))