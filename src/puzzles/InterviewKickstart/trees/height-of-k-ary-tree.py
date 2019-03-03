# Complete the function below.

'''
    For your reference:

    class TreeNode:
        def __init__(self):
            self.children = []

'''

def rec(root):
    if root is None:
        return 0
    else:
        if len(root.children) > 0:
            return max((rec(c) for c in root.children)) + 1
        else:
            return 1

def find_height(root):
    # I disagree with the solution's definition of height, so I had to correct my
    # solution with the -1
    return rec(root)-1
