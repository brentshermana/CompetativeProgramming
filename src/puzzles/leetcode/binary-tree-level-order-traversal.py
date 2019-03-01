# return a list containing the level-order traversal, from left to right
# each level is also a list, so the

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root):
        result = []

        next_level = deque()
        level = deque()
        if root is not None:
            level.appendleft(root)

        while len(level) > 0: # for each level
            level_result = []
            while len(level) > 0: # for each element in current level
                n = level.pop()
                level_result.append(n.val)
                for c in (n.left, n.right):
                    if c is not None:
                        next_level.appendleft(c)
            # store this level
            result.append(level_result)
            # reset queues
            level = next_level
            next_level = deque()
        return result

n = TreeNode(1)
n.left = TreeNode(3)
n.right = TreeNode(2)
n.left.left = TreeNode(4)

print(Solution().levelOrder(n))
