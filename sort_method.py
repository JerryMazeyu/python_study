# 选择排序

def exchange(list, a, b):
    """简单交换"""
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
    return list

def select_sort(list):
    """选择排序"""
    n = len(list)
    for j, num in enumerate(list):
        min = list[j]
        min_index = j
        for i in range(j+1, n):
            if min >= list[i]:
                min_index = i
                min = list[i]
        exchange(list, j, min_index)
    return list

def insert_sort(list):
    """插入排序"""
    n = len(list)
    for i in range(n):
        for j in range(i-1, -1, -1):
            if list[i] < list[j]:
                exchange(list,i,j)
                i = j
    return list

def merge(lista, listb):
    """合并两个有序数组"""
    res = []
    i = 0
    j = 0
    cur1 = lista[i]
    cur2 = listb[j]
    while True:
        if cur1 >= cur2:
            res.append(cur2)
            try:
                cur2 = listb[j + 1]
                j += 1
            except:
                for k in range(i, len(lista)):
                    res.append(lista[k])
                return res
        else:
            res.append(cur1)
            try:
                cur1 = lista[i + 1]
                i += 1
            except:
                for k in range(j, len(listb)):
                    res.append(listb[k])
                return res

def recrusion_sort(list):
    """归并排序"""
    n = len(list)
    if n == 1:  # 等于1的时候返回列表本身
        return list
    if n == 2:  # 等于2的时候也可以返回
        if list[0] > list[1]:
            temp = list[0]
            list[0] = list[1]
            list[1] = temp
        else:
            pass
        return list  # 这一部分保证最基本的列表是有序的
    apart = recrusion_sort(list[0: round(n / 2)])  # 将前半部分分割成一部分，调用这个函数
    bpart = recrusion_sort(list[round(n / 2): n])  # 将后半部分分割成一部分，现在可以认为这个abpart都排序了
    return merge(apart, bpart)  # 合并两个有序数组





def quick_sort_part(list):  # 快速排序，思路参考https://blog.csdn.net/morewindows/article/details/6684558
    n = len(list)  # 这一部分定义1，2的情况
    if n == 1:
        return list
    elif n == 2:
        if list[0] > list[1]:
            temp = list[0]
            list[0] = list[1]
            list[1] = temp
        else:
            pass
        return list

    temp = list[0]  # 这一部分定义递归的部分
    i = 0
    j = len(list)-1
    while True:
        while True:  # 从后向前的部分
            cur2 = list[j]
            if cur2 <= temp:
                list[i] = cur2
                break
            else:
                j -= 1
                if i == j:
                    list[j] = temp  # 此时第一个已经找到正确索引，我们把处理好的分成左右，分别递归调用，使左右两边都排好序，最后一加就好了。
                    try:
                        right = quick_sort_part(list[0:j])
                    except:
                        right = []
                    try:
                        left = quick_sort_part(list[j + 1:])
                    except:
                        left = []
                    return right + [list[j]] + left
        while True:  # 从前往后部分
            cur1 = list[i]
            if cur1 > temp:
                list[j] = cur1
                break
            else:
                i += 1
                if i == j:
                    list[j] = temp
                    try:
                        right = quick_sort_part(list[0:j])
                    except:
                        right = []
                    try:
                        left = quick_sort_part(list[j + 1:])
                    except:
                        left = []
                    return right + [list[j]] + left




a = [3,4,5,324,2,3,4,56,9,4,22,24,6,3]
print(quick_sort_part(a))