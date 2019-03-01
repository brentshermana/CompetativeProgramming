# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive solution: works fine

def symmetric_eq(a, b):
    if a is None or b is None:
        return a is None and b is None
    return a.val==b.val and symmetric_eq(a.left, b.right) and symmetric_eq(a.right, b.left)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root is None or symmetric_eq(root.left, root.right)

# iterative solution is a little more interesting to code:
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while len(stack) > 0:
            a, b = stack.pop()
            if a is None or b is None:
                if a != b:
                    return False
            else:
                if a.val != b.val:
                    return False
                stack.append((a.right, b.left))
                stack.append((a.left, b.right))
        return True
