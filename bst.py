#Binary Search tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)

    else:
        if root.val < key:
            root.right = insert(root.right, key)

        else:
            root.left = insert(root.left, key)

    return root

def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)

def tree_sort(arr):
    res = []
    root = None

    for i in arr:
        root = insert(root, i)

    inorder(root, res)

    return res

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", tree_sort(arr))
