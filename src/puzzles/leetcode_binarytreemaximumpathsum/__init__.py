# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# Example 1:
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42


# SOLVED
# here's the idea: although a path is not necessarily containing the root node, it must
# by definition have some highest node. So we can implement the solution recursively,
# working our way up from trivial leaf solutions



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        best = -math.inf

        def rec(root):
            if root == None: return 0

            leftmax = rec(root.left)
            rightmax = rec(root.right)

            rootmax = root.val # the max value of a path rooted at this node
            # we don't need to include paths in the subtree if they're not good
            if leftmax > 0:
                rootmax += leftmax
            if rightmax > 0:
                rootmax += rightmax

            # overwrite the highest path value if this is it
            nonlocal best
            best = max(best, rootmax)

            # as a fraction of a greater path, we can only include one of the two child paths
            # (but still don't have to include either)
            return root.val + max(rightmax, leftmax, 0)

        rec(root)
        return best