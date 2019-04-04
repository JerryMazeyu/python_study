class BiTNode(object):
    def __init__(self):
        self.item = None
        self.lchild = None
        self.rchild = None

class FindMaxSubTree(object):
    def __init__(self):
        node = BiTNode()
        self.root = node
        self.max = 1e-30
        self.max_list = []

    def breadth_add(self, item):
        """广度优先插入数据"""
        node = BiTNode()
        node.item = item
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

    def print_tree_layer(self, root):
        """广度优先遍历树"""
        if root.item is None:
            return
        else:
            q = [root]
        while q:
            cursor = q.pop(0)
            try:
                print(cursor.item, "->", end=" ")
            except:
                pass
            try:
                q.append(cursor.lchild)
            except:
                pass
            try:
                q.append(cursor.rchild)
            except:
                pass

    def is_not_none(self, n):
        if n is not None:
            return n

    def find_max_sub_tree(self, root):
        """查看最大子树和"""
        if root.lchild is not None:
            lmax = self.find_max_sub_tree(root.lchild)
        else:
            lmax = None
        if root.rchild is not None:
            rmax = self.find_max_sub_tree(root.rchild)
        else:
            rmax = None
        temp = filter(self.is_not_none, [rmax, lmax])  # 找出不是none的所有值
        tmax = sum(temp) + root.item
        # print("lmax, rmax, tmax: ", lmax, rmax, tmax)
        temp_1 = filter(self.is_not_none, [rmax, lmax, tmax])
        self.max = max(temp_1)
        # print("self.max: ", self.max)
        return self.max

if __name__ == '__main__':
    tree = FindMaxSubTree()
    num = [1, 9, -7, -3, 6]
    for i in num:
        tree.breadth_add(i)
    tree.print_tree_layer(tree.root)
    print("")
    tree.find_max_sub_tree(tree.root)
    print(tree.max)