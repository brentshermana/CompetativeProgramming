# GOT IT.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: 'int') -> 'List[TreeNode]':
        if N % 2 == 0:
            # N must be odd
            return []
        # we're going to reuse subtrees to save on space/time
        mem = {}

        def rec(n):
            if n in mem:
                return mem[n]
            if n == 1:
                return [TreeNode(0)]

            children = n-1
            # only iterate through odd numbers. Otherwise the
            # subtrees won't be full!
            result = []
            for l in range(1, children, 2):
                r = children-l
                ls = rec(l)
                rs = rec(r)
                for lchild in ls:
                    for rchild in rs:
                        root = TreeNode(0)
                        root.right = rchild
                        root.left = lchild
                        result.append(root)
            mem[n] = result
            return result

        return rec(N)
