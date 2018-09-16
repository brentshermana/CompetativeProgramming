# Given a binary tree, find the length of the longest consecutive sequence path.
#
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
#
# Example 1:
#
# Input:
#
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
#
# Output: 3
#
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
# Example 2:
#
# Input:
#
#    2
#     \
#      3
#     /
#    2
#   /
#  1
#
# Output: 2
#
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

# DONE
# logic: when iterating recursively from parents to children, and given the parent's value and
# the size of the current sequence, we know what the new sequence size is.
# Just keep track of the maximum value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0

        def rec(root, cur_len=0, parent_val=None):
            if root == None:
                return

            elif parent_val == root.val - 1:
                new_len = cur_len + 1
            else:
                new_len = 1
            self.longest = max(self.longest, new_len)
            rec(root.left, new_len, root.val)
            rec(root.right, new_len, root.val)

        rec(root)
        return self.longest