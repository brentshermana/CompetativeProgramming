# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

# DONE: reduces to same problem as 'binary tree maximum path sum', so just refer to that explanation

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.best = 0

        def rec(root, nesting=0):
            if root == None: return 0

            bestleftcomponent = rec(root.left, nesting + 1)
            bestrightcomponent = rec(root.right, nesting + 1)

            self.best = max(self.best, bestleftcomponent + bestrightcomponent)
            # print('{}local size: {} returning {}'.format('\t'*nesting, bestleftcomponent + bestrightcomponent + 1, max(bestleftcomponent, bestrightcomponent) + 1))
            return max(bestleftcomponent, bestrightcomponent) + 1

        rec(root)
        return self.best