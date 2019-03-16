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

    def reindex(self, head):
        cur1 = head  # 这个指针是正向的遍历指针
        next = cur1.next
        cur2 = cur1  # 这个指针是逆向的遍历指针
        stop_after = False  # 这是一个退出的条件
        if not head.next:  # 对于单个节点
            return head
        while True:
            while True:  # 这个循环找出倒数第一、第二个节点
                if not cur2.next.next:
                    pre = cur2
                    cur2 = cur2.next
                    break
                else:
                    cur2 = cur2.next
            if next == pre:  # 如果发现倒数第二个和遍历的正数第二个重合，经过一次变换即可得到结果，如15234N
                stop_after = True
            elif next == cur2:  # 如果正数第二和倒数第一已经重合，说明搞定了，适用于偶数节点，如1423N
                break
            cur1.next = cur2  # 这些步骤两个目的，第一把指针改变，第二是做下一步的准备
            cur2.next = next
            pre.next = None
            cur1 = next
            next = cur1.next
            cur2 = cur1
            if stop_after:  # 如果刚才这个变量为True，那么就停止
                break
        return head



if __name__ == '__main__':
    ListNode_1 = ListNodeHandle()
    l1 = ListNode(None)
    l1_list = [4, 3, 2, 1]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    ListNode_1.printNodelist(l1)
    print("+" * 50)
    l2 = ListNode_1.reindex(l1)
    print("+" * 50)
    ListNode_1.printNodelist(l2)
