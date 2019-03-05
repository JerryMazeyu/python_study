# 从命令行接受一个整数N，在单位正方形中生成N个随机点，然后计算两点之间最近距离。
import random
import numpy
import matplotlib.pyplot as plt

def Piont2D(n):
    x = []
    y = []
    min_distance = numpy.sqrt(2)
    for i in range(n):
        x.append(random.uniform(0, 1))
        y.append(random.uniform(0, 1))
    for i in range(n):
        for j in range(n):
            if i == j:  # 注意如果不加这个就会变成0
                continue
            distance = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            if distance <= min_distance:
                x_min = [x[i], x[j]]
                y_min = [y[i], y[j]]
                min_distance = distance
    plt.xlim(xmax=1, xmin=0)
    plt.xlim(xmax=1, xmin=0)
    plt.plot(x, y, 'ro')
    plt.plot(x_min, y_min, c='r')
    plt.show()
    print(min_distance)
    return min_distance

Piont2D(10)