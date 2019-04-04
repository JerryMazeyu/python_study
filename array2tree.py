class BiTNode(object):
    def __init__(self):
        self.item = None
        self.lchild = None
        self.rchild = None


def array2tree(array, start, end):
    """将有序数组转化为二叉树（搜索树）"""
    root = None
    if end >= start:
        root = BiTNode()
        mid = (start + end + 1) // 2
        root.item = array[mid]
        root.lchild = array2tree(array, start, mid-1)
        root.rchild = array2tree(array, mid+1, end)
    else:
        root = None
    return root


def mid_order(root):
    """中序遍历"""
    if root is None:
        return
    else:
        mid_order(root.lchild)
        print(root.item, "-> ", end="")
        mid_order(root.rchild)
        return

def print_tree_layer(root):
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


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tree = array2tree(arr, 0, len(arr)-1)
    mid_order(tree)
    print("")
    print_tree_layer(tree)