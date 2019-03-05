# 寻找一个数组，输出和为target的下标。

def add_target(lst, target):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(n-i-1):
            if lst[i] + lst[n-j-1] == target:
                # print(i, n-j-1)
                result.append([i,n-j-1])
    return result


print(add_target(range(100), target=5))