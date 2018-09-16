# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
#
# Example:
#
# Input:
#
#    1
#     \
#      3
#     /
#    2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
# Note: There are at least two nodes in this BST.

# SUCCESS. Just do an inorder traversal and examine difference between consecutive values


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math


class Solution:

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def inorder(root):
            if root != None:
                yield from inorder(root.left)
                yield root.val
                yield from inorder(root.right)

        ret = math.inf
        prev = None
        for v in inorder(root):
            if prev == None:
                prev = v
            else:
                ret = min(ret, abs(prev - v))
                prev = v
        return ret