# This problem statement is pretty stupid.
# given a binary tree where all the right nodes are leaf nodes, flip it upside down
# into a binary tree with left leaf nodes

# class TreeNode():
    # def __init__(self, val=None, left_ptr=None, right_ptr=None):
    #     self.val = val
    #     self.left_ptr = left_ptr
    #     self.right_ptr = right_ptr

# for each root, right, left
# disconnect root from right and left
# connect left.left to right
# connect left.right to root

def rec(root, left, right):
    if left is None:
        return root
    leftleft = left.left_ptr
    leftright = left.right_ptr

    # if this is not true, the root was a "left" of a previous call,
    # so its pointers already have valid values
    if root.left_ptr == left:
        root.left_ptr = None
        root.right_ptr = None
    left.left_ptr = right
    left.right_ptr = root
    return rec(left, leftleft, leftright)


def flipUpsideDown(root):
    if root is None:
        return None
    return rec(root, root.left_ptr, root.right_ptr)
