# 最近在看一些和链表相关的算法脚本，python中本来没有链表结构，但是操作却体现了很多C中的思想。
# 首先，链表是一种不连续储存的数据结构，每一个链包含一个数据结构和一个指针，那么他可以实现一些很有趣的操作，
# 比如当插入或者删除一个元素时，他的复杂度仅为O(1)，而列表是O(n)。但是于此同时，查询则变得十分复杂，因为要从头查起。
# 现在我要做的是在py中模拟链表的数据结构，对他进行定义、添加元素、顺序打印与实现逆序的操作。
# 这么做的难度在于python中没有独立的指针概念，任何一个变量都是指针，
# 所以a = b 除了理解为将b赋值给a外，还可以理解为指针a指向了b，这么理解的话，我想这些算法就变得易于理解了。


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

    def _reverse(self, nodelist):
        """逆序链表"""
        cur_node = nodelist  # 将光标移动到开头
        i = 0  # 设置一个哨兵变量
        while cur_node.next:  # 当下一个还有的时候
            next_node = cur_node.next  # 先定义另一个指针，指向下一个节点
            reversenode = ListNode()  # 新定义一个reverse链表，并创建一个不带链的、以next_node.val为val的节点
            reversenode.val = next_node.val
            if i == 0:  # 如果是第一次的话
                reversenode.next = ListNode()  # 令这个reverse的next指向一个新创建的cur_node.val的节点
                reversenode.next.val = cur_node.val
                temp_1 = reversenode  # 此时新定义一个指针，指向了这个带两个链的链表
            else:
                reversenode.next = temp_1  # 如果不是第一次，则直接新建的节点指向前面已经创建好的链表
                temp_1 = reversenode  # 在将做好的迭代进去，可以认为temp_1是一个缓存区，每次检索到下一个，再把上一次做好的添加进去
            cur_node = cur_node.next  # 移动光标
            i += 1
        return reversenode



if __name__ == '__main__':
    ListNode_1 = ListNode_handle()
    l1 = ListNode()
    l1_list = [1, 8, 3, 4]
    for i in l1_list:
        l1 = ListNode_1.add(i)
    l2 = ListNode_1._reverse(l1)
    ListNode_1.printNodelist(l1)
    ListNode_1.printNodelist(l2)