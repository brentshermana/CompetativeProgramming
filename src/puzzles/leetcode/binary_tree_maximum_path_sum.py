# This problem isn't too hard, but identifying that it was necessary to return
# two values, and catching all the edge cases required many failed submissions,
# so I would overall regard my attempt as a failure



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# problem with recursive formulation: some solutions can be passed up, others can't
# this depends on whether the root is contained within the

import math

def helper(root):
    """
    return two values: the best sum which can be used by the caller to build up a solution,
                       and the best sub in this subtree overall

    the latter is necessary because it may be the best path overall, and needt to be returned somehow
    """
    if root is None:
        return -math.inf, -math.inf
    else:
        left_inc, left_best = helper(root.left)
        right_inc, right_best = helper(root.right)

        # produce the best path that includes the root
        # because inc needs to be able to "attach" to parent trees,
        # we can include the left child OR the right child, but not both
        inc = root.val + max(left_inc, right_inc, 0)

        # produces the best path that might not contain the root
        # we only need to consider left_best, right_best, and inc because
        # inc is the max of any combination of left,right,root containing root
        best_withroot = root.val
        if left_inc > 0:
            best_withroot += left_inc
        if right_inc > 0:
            best_withroot += right_inc
        best = max(left_best, right_best, best_withroot)

        return inc, best


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return helper(root)[1]
