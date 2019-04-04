class DoubleQueue(object):
    """双向队列"""
    def __init__(self):
        """存储数据的私有变量"""
        self.__list = []

    def is_empty(self):
        """判断是否为空"""
        return self.__list == []

    def travel(self):
        """遍历队列"""
        print(self.__list)


    def add(self, item):
        """头部入队"""
        self.__list.insert(0, item)
        return self.__list

    def append(self, item):
        """尾部入队"""
        self.__list.append(item)
        return self.__list

    def pop(self):
        """队尾出队"""
        if self.is_empty():
            return
        return self.__list.pop()

    def pop0(self):
        """队头出队"""
        if self.is_empty():
            return
        return self.__list.pop(0)

    def size(self):
        """查看队列大小"""
        return len(self.__list)

    def clear(self):
        """清空队列"""
        for i in range(self.size()):
            self.pop()
        return self.__list

if __name__ == '__main__':
    dq = DoubleQueue()
    print(dq.is_empty())
    dq.add(10)
    dq.append(11)
    dq.add(9)
    dq.clear()
    dq.travel()
    # dq.pop()
    # dq.pop0()
    # print(dq.is_empty())
    # dq.travel()




