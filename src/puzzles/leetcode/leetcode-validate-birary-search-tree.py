# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math

class Solution:
    # The key here is tracking the "bounds" which subtree values must fall under
    def isValidBST(self, root, base=-math.inf, cap=math.inf):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # will only happen on the "original" call, since we perform null
        # checks on subsequent calls
        if root is None:
            return True
        if root.val <= base or root.val >= cap:
            return False
        
        valid = True
        if root.left:
            valid = valid and self.isValidBST(root.left, base=base, cap=root.val)
        if root.right:
            valid = valid and self.isValidBST(root.right, base=root.val, cap=cap)
        return valid