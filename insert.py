class ListNode():
    def __init__(self, val=None):
        self.val = val
        self.next = None


class ListNodeHandle():
    def tail_insert(self, head: ListNode, data):
        cur = head
        while cur.next:
            cur = cur.next
        data = ListNode(data)
        cur.next = data
        return head

    def head_insert(self, head: ListNode, data):
        data = ListNode(data)
        data.next = head
        head = data
        return head

    def print_list(self, head):
        print("+" * 50)
        cur = head
        while cur is not None:
            print(cur.val)
            cur = cur.next
        print("+" * 50)


if __name__ == '__main__':
    # l1 = ListNode(1)
    lh = ListNodeHandle()
    # for i in [3, 5, 7, 9]:
    #     l1 = lh.tail_insert(l1, i)
    l1 = ListNode(9)
    for i in [7, 5, 3, 1]:
        l1 = lh.head_insert(l1, i)
    lh.print_list(l1)