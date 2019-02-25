# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def reverse_order(root):
    if root:
        yield from reverse_order(root.right)
        yield root
        yield from reverse_order(root.left)

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        gsum = 0
        for n in reverse_order(root):
            orig_nval = n.val
            n.val += gsum
            gsum += orig_nval
        return root