# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def countX(n, val=None):
    if n is None:
        return 0, []
    elif val != None and val != n.val:
        return 0, [n]

    lcount, ltrees = countX(n.left, n.val)
    rcount, rtrees = countX(n.right, n.val)

    ltrees.extend(rtrees)

    return lcount + rcount + 1, ltrees

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        modes = []
        mode_count = 0
        stack = [root]

        while len(stack) > 0:
            n = stack.pop()
            count, trees = countX(n)
            stack.extend(trees)

            if count == mode_count:
                modes.append(n.val)
            elif count > mode_count:
                modes = [n.val]
                mode_count = count

        return modes

