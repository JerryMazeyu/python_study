# 寻找两个非负整数p，q数的最大公约数，若q为0，则最大公约数为p。否则，将p除以q得到余数r，pq的最大公约数为qr最大公约数。
def gcd(p_temp, q_temp):
    p = max(p_temp, q_temp) # 这里要记得不能没有_temp下标，否则值被迭代了。
    q = min(p_temp, q_temp)
    if q == 0:
        g = p
    else:
        r = p % q
        g = gcd(r, q)
    return g

print(gcd(8,4))