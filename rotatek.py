# 旋转链表。

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class ListNodeHandle(object):
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        node = ListNode(data)
        node.next = self.cur_node
        self.cur_node = node
        return node

    def printNodelist(self, nodelist):
        cur_node = nodelist
        while cur_node:
            print("val: ", cur_node.val, "next: ", cur_node.next)
            cur_node = cur_node.next

    def findlastk(self, head:ListNode, k):  # 快慢指针
        cur1 = head
        cur2 = head
        i = 0
        while True:
            cur1 = cur1.next
            i += 1
            if i >= k:
                cur2 = cur2.next
            if not cur1.next:
                return cur2.val


    def rotatek(self, head, k):
        cur1 = head
        cur2 = head
        i = 0
        while True:
            cur1 = cur1.next
            i += 1
            if i >= k + 1:
                cur2 = cur2.next
            if not cur1.next:
                pre = cur2
                cur2 = cur2.next
                cur1.next = head
                pre.next = None
                return cur2


if __name__ == '__main__':
    ListNode_1 = ListNodeHandle()
    l1 = ListNode(None)
    l1_list = [7, 6, 5, 4, 3, 2, 1]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    ListNode_1.printNodelist(l1)
    print("+" * 50)
    # l2 = ListNode_1.reindex(l1)
    # print("+" * 50)
    # ListNode_1.printNodelist(l2)

    l3 = ListNode_1.rotatek(l1, 3)
    ListNode_1.printNodelist(l3)