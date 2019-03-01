# complete this function

'''
    For your reference:

    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''
def rec(a, base, cap):
    if base >= cap:
        return None
    mid = (base+cap)//2
    n = TreeNode(a[mid])
    n.left_ptr = rec(a, base, mid)
    n.right_ptr = rec(a, mid+1, cap)
    return n

def build_balanced_bst(a):
    return rec(a, 0, len(a))
