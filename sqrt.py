# 牛顿迭代求平方根，迭代式为x(n+1)=x(n)－f(x(n))/f'(x(n))，设某数为p，则有方程f（x）= x^2-p，方程的0根即为所求数的平方根，根据牛顿迭代的原理，可以得到以下的迭代公式，X(n+1)=[X(n)+p/Xn]/2，这里面p就是要求平方根的数字
def sqrt(n):
    e = 1e-10  # 注意表达式
    q = n
    while abs(q*q - n) > e:
        q = (q + n/q) / 2
    return q

print(sqrt(4))