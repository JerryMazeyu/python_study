class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class CycleListNode(object):
    def __init__(self, node=None):
        """定义循环链表"""
        node = Node(node)
        self.__head = node
        if node:
            node.next = self.__head


    def is_empty(self, verbose = False):
        """查看链表是否为空"""
        if verbose:
            print("is empty? ", self.__head is None)
        return self.__head is None

    def length(self):
        """查看链表长度"""
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            cur = cur.next
            count += 1
        print("count is: ", count)
        return count

    def travel(self):
        """遍历循环单链表"""
        if self.is_empty():
            return
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.item, "->", end=" ")
                cur = cur.next
            print(cur.item)

    def add(self, item):
        """向头部追加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            rear = self.__head
            while rear.next != self.__head:
                rear = rear.next
            node.next = self.__head
            rear.next = node
            self.__head = node
        return self.__head

    def append(self, item):
        """向尾部追加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            rear = self.__head
            while rear.next != self.__head:
                rear = rear.next
            rear.next = node
            node.next = self.__head
        return self.__head

    def insert(self, item, position):
        """在指定位置插入链表元素"""
        node = Node(item)
        n = self.length()
        if position > n+1:
            print("position false!")
            return
        elif position == 1:
            self.add(item)
        else:
            cur = self.__head
            pre = cur
            count = 1
            start = False
            while count != position:
                cur = cur.next
                if start:
                    pre = pre.next
                start = True
                count += 1
            pre.next = node
            node.next = cur
            return self.__head

    def search(self, item, verbose=False):
        """查找链表中是否有此元素"""
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                if verbose:
                    print("True")
                return True
            cur = cur.next
        if verbose:
            print(cur.item == item)
        return cur.item == item

    def remove(self, position):
        """删除指定位置的元素"""
        if self.is_empty():
            return
        elif position == 1 and self.length() != 1:
            rear = self.__head
            while rear.next != self.__head:
                rear = rear.next
            self.__head = self.__head.next
            rear.next = self.__head
            return self.__head
        elif position == 1 and self.length() == 1:
            self.__head = None
            return self.__head
        else:
            cur = self.__head
            pre = self.__head
            count = 1
            start = False
            while count != position:
                cur = cur.next
                if start:
                    pre = pre.next
                start = True
                count += 1
            pre.next = cur.next




if __name__ == '__main__':
    cln = CycleListNode(10)
    cln.is_empty(verbose=True)
    cln.travel()
    cln.length()
    cln.add(19)
    cln.is_empty(verbose=True)
    cln.length()
    cln.travel()
    cln.append(12)
    cln.is_empty(verbose=True)
    cln.length()
    cln.travel()
    cln.insert(99, 2)
    cln.insert(999, 5)
    cln.insert(0, 1)
    cln.is_empty(verbose=True)
    cln.length()
    cln.travel()
    cln.search(0, verbose=True)
    cln.remove(1)
    cln.travel()