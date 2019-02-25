# Given a binary tree, we need to count the number of unival subtrees
# (all nodes have the same value)
#
# Example: the following tree has THREE unival subtrees
#   5
# 5   5
# the root, and each leaf is counted distinctly



# class TreeNode():
#     def __init__(self, val=None, left_ptr=None, right_ptr=None):
#         self.val = val
#         self.left_ptr = left_ptr
#         self.right_ptr = right_ptr

# returns (count, val, is_unival)
def rec(rt):
    if rt == None:
        return 0, None, True

    lc, lv, lu = rec(rt.left_ptr)
    rc, rv, ru = rec(rt.right_ptr)

    if not ru or not lu:
        return lc+rc, rt.val, False
    elif (rv is None or rv == rt.val) and (lv is None or lv == rt.val):
        return lc+rc+1, rt.val, True
    else:
        return lc+rc, rt.val, False

# entry point function
def findSingleValueTrees(root):
    return rec(root)[0]
