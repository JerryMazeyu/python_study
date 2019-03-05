# 从命令行输入一个整数N，从标准输入中读取N个间隔，打印所有相交的间隔。
import random
def Interval1D(n):
    x = []
    y = []
    result_index = []
    for i in range(n):
        x_temp = random.randint(0, 100)
        y_temp = random.randint(0, 100)
        x.append(min(x_temp, y_temp))
        y.append(max(x_temp, y_temp))
    for i in range(n):
        print(x[i], y[i])
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                if y[j] >= y[i] >= x[j] or y[j] >= y[i] >= x[j]:
                    if [min(i, j), max(i, j)] in result_index:
                        pass
                    else:
                        result_index.append([min(i, j), max(i, j)])
                elif y[i] >= y[j] >= x[i] or y[i] >= y[j] >= x[i]:
                    if [min(i, j), max(i, j)] in result_index:
                        pass
                    else:
                        result_index.append([min(i, j), max(i, j)])
    for i in range(len(result_index)):
        print(x[result_index[i][0]], y[result_index[i][0]], "&", x[result_index[i][1]], y[result_index[i][1]])

Interval1D(5)