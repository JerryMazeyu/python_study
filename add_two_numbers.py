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

    def _reverse(self, head: ListNode):
        cur = head
        next = cur.next
        i = 0
        while next:
            if i == 0:
                cur.next = None
                i += 1
            temp = next.next
            next.next = cur
            cur = next
            next = temp
        return cur

    def _add_two_numbers(self, head1, head2):  # 想了很久，还是决定做双重循环。
        head1 = self._reverse(head1)
        head2 = self._reverse(head2)
        cur1 = head1
        cur2 = head2
        isaddone = 0
        while True:
            if cur1 and cur2:
                cur2.val = cur1.val + cur2.val + isaddone
                isaddone = 0
                if cur2.val >= 10:
                    cur2.val = cur2.val % 10
                    isaddone = 1
                pre1 = cur1
                pre2 = cur2
                cur2 = cur2.next
                cur1 = cur1.next

            elif cur1 and not cur2:
                cur2 = ListNode(cur1.val + isaddone)
                pre2.next = cur2
                isaddone = 0
                if cur2.val >= 10:
                    cur2.val = cur2.val % 10
                    isaddone = 1
                cur2 = cur2.next
                cur1 = cur1.next

            elif cur2 and not cur1:
                cur2.val = cur2.val + isaddone
                isaddone = 0
                cur2 = cur2.next

            else:
                break
        return self._reverse(head2)

    def isloop(self, head):
        cur = head.next
        while True:
            if cur is head:
                return True
            elif not cur:
                return False
            else:
                cur = cur.next




if __name__ == '__main__':
    ListNode_1 = ListNodeHandle()
    l1 = ListNode(None)
    l1_list = [3, 7, 4]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    ListNode_1.printNodelist(l1)
    print("+"*50)
    # l2 = ListNode_1._reverse(l1)
    # ListNode_1.printNodelist(l2)
    l2 = ListNode(4)
    cur = l2
    l2.next = ListNode(9)
    l2.next.next = ListNode(7)
    l2.next.next.next = cur
    # ListNode_1.printNodelist(l2)
    print("+" * 50)
    # l3 = ListNode_1._add_two_numbers(l1, l2)
    # ListNode_1.printNodelist(l3)
    print(ListNode_1.isloop(l2))