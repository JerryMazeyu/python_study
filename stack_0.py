class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """压栈"""
        self.__list.append(item)

    def pop(self):
        """弹栈"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty():
            return None
        else:
            return self.__list[-1]

    def is_empty(self):
        """查看是否是空栈"""
        return self.__list == []

    def size(self):
        """查看栈的元素个数"""
        return len(self.__list)

    def print(self):
        """查看栈的全部元素"""
        print(self.__list)


if __name__ == "__main__":
    s1 = Stack()
    for i in [1,3,5,7]:
        s1.push(i)
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    # s1.print()