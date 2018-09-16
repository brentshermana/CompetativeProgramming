# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# ^^^ to make the search log(n) per query, each node must track the size of its subtree (this is possible),
# so you can track the 'sum' of all subtrees to the left of your target value, and only have to iterate down
# one chain!



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def tree_iter(root):
    if root != None:
        yield from tree_iter(root.left)
        yield root.val
        yield from tree_iter(root.right)

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = 1
        for val in tree_iter(root):
            if count == k:
                return val
            else:
                count += 1