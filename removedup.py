# 希望实现链表的正向去重，例如1->2->1->4，可以输出2->1->4。这里用到了双重循环，并且定义了很多指针，
# cur是外部循环的指针，temp是内部循环的指针，next指向外部循环的下一个node，beg为返回值的head为第一个需要的值，pre记录最后的一个需要的值。
# 实现起来逻辑很复杂，中间打了很多点去debug，总之，需要把握的要点有：
# 1 双重循环
# 2 内部循环分为三类，第一类是temp循环到结尾了，意味着cur没重复，第二类是temp和cur相等，意味着cur有重复，第三类既不相等也不结尾，那么进行temp的下一次移动。
# 3 pre在cur要的时候需要跟进cur，然后cur进行下一个，如果不要的话要用到pre，删除位于中间的cur元素。
# 4 beg只记录第一次cur要的时候，这时候用一个变量做哨兵。

class ListNode(object):
    """定义一个单链表的数据结构，这里定义了一个类，每一个实例的结构都是带有val和next属性的，默认都为None。"""
    def __init__(self):
        self.val = None
        self.next = None

class ListNode_handle:
    """这里定义了一个操作类，所有的操作都在这边实现。"""
    def __init__(self):
        self.cur_node = None  # 这个就是一个典型的指针，类似于光标，表示我们现在再对谁进行操作。

    def add(self, data):
        """向前添加一个指定的元素"""
        node = ListNode()  # node是一个链的节点
        node.val = data  # 设置他的value
        node.next = self.cur_node  # 注意这里是指向了当前的节点，第一次是None，而第二次就不是了，self.cur_node可以是一个连了很长的链表。
        self.cur_node = node  # 此时将光标移动至新建的那个节点上（可能后面跟了一大串，便于处理
        return node  # 返回那个新的链表

    def printNodelist(self, nodelist):
        """顺序输出链表"""
        cur_node = nodelist  # 重新定义光标变量，不作为类属性
        while cur_node:  # 当光标还存在时（最后变None）
            print("val: ", cur_node.val, "   next: ", cur_node.next)  # 输出当前的value和指针
            cur_node = cur_node.next  # 将光标移动到下一个，注意此处不是nodelist.next，这里的nodelist可以视作一个变量，不可看作指针


def removeDup(head:ListNode):
    """顺序遍历去重链表"""
    cur = head
    if cur.next is None:
        return head
    else:
        beg = head
        pre = head
        i = 0
        while cur.next is not None:
            print("a", cur.val)
            next = cur.next
            temp = cur.next
            while True:
                print("b")
                try:  # 这里防止报错temp = None
                    tempval = temp.val
                except:
                    tempval = None
                if tempval == cur.val:
                    print("c")
                    if pre == cur:  # 这也就是意味着cur前面没有要的元素，那么pre继续跟进cur
                        print("c1")
                        cur.next = None
                        cur = next
                        pre = cur
                    else:  # 这意味着pre前面有要的元素，这是cur进行到了下一个元素，这个元素不确定是否在这边，所以pre不动。
                        print("c2")
                        cur.next = None
                        pre.next = next
                        cur = next
                    break
                elif temp is None:
                    print("d")
                    if i == 0:
                        print("e")
                        beg = cur
                        i += 1
                    pre = cur  # 这时代表这个元素没有重复，pre要跟上。
                    cur = next
                    break
                else:
                    print("f")
                    temp = temp.next
    return beg

if __name__ == '__main__':
    ListNode_1 = ListNode_handle()
    l1 = ListNode()
    l1_list = [2,2,3,1,1,5,3]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    ListNode_1.printNodelist(l1)
    print("+"*50)
    l2 = removeDup(l1)
    ListNode_1.printNodelist(l2)
