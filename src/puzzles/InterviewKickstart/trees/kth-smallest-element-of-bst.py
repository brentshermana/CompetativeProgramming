'''
    For your reference:

    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

def inorder(root):
    if root == None:
        return
    yield from inorder(root.left_ptr)
    yield root.val
    yield from inorder(root.right_ptr)

def kth_smallest_element(root, k):
    it = inorder(root)
    # consume the first k-1
    for _ in range(k-1):
        next(it)
    # the next one will be the k-th
    return next(it)
