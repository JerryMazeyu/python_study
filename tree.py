from double_queue import DoubleQueue
class Node(object):
    """定义树的节点"""
    def __init__(self, item=None):
        self.item = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        node = Node()
        self.root = node
        self.q = DoubleQueue()

    def breadth_add(self, item):
        """广度优先插入数据"""
        node = Node(item)
        if self.root.item is None:
            self.root = node
            return self.root
        else:
            q = [self.root]
            while True:
                target = q.pop(0)
                if target.lchild is None:
                    target.lchild = node
                    return
                elif target.rchild is None:
                    target.rchild = node
                    return
                else:
                    q.append(target.lchild)
                    q.append(target.rchild)

    def breadth_travel(self):
        """广度优先遍历树"""
        if self.root is None:
            return
        else:
            q = [self.root]
        while q:
            cursor = q.pop(0)
            if cursor is None:
                print(" ")
                return
            else:
                print(cursor.item, "-> ", end="")
                q.append(cursor.lchild)
                q.append(cursor.rchild)

    def pre_order(self, root):
        """先序遍历"""
        if root is None:
            return
        else:
            print(root.item, "-> ", end="")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)
            return

    def mid_order(self, root):
        """中序遍历"""
        if root is None:
            return
        else:
            self.mid_order(root.lchild)
            print(root.item, "-> ", end="")
            self.mid_order(root.rchild)
            return

    def post_order(self, root):
        """后序遍历"""
        if root is None:
            return
        else:
            self.mid_order(root.lchild)
            self.mid_order(root.rchild)
            print(root.item, "-> ", end="")
            return

    def is_post_order(self, list, start, end):
        """判断一个数组是否是二元查找树后序遍历的序列"""
        root = list[end]
        if list[start:end] == [] or len(list[start:end+1]) < 3:
            return True
        for i in list[start:end]:
            if i > root:
                split = list.index(i)
                break
        self.is_post_order(list, start, split-1)
        self.is_post_order(list, split, end-1)
        if min(list[split: end]) >= root:
            return True
        else:
            # print("False")
            return False


if __name__ == '__main__':
    tree = Tree()
    tree.breadth_add('A')
    tree.breadth_add('B')
    tree.breadth_add('C')
    tree.breadth_add('D')
    tree.breadth_add('E')
    tree.breadth_add('F')
    tree.breadth_travel()
    tree.pre_order(tree.root)
    print("")
    tree.mid_order(tree.root)
    print("")
    tree.post_order(tree.root)
    print("")
    print(tree.is_post_order([1, 3, 2, 5, 7, 6, 4], 0, 6))