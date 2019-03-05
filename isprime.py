# 判断一个数n是否为素数，从2到根号n，都除以，如果除不尽就是素数。
def isPrime(n):
    i = 2
    result = True
    while i*i <= n:  # 注意这个等号
        r = n % i
        if r == 0:
            result = False
            break
        i = i + 1
    return result

print(isPrime(9))
