# return the VALUE of the least common ancestor of the two given nodes.
# this is NOT a binary search tree, just a binary tree

#class Node(object):
#    def __init__(self, data, left=None, right=None):
#        self.data = data
#        self.left = left
#        self.right = right

# returns True when the path has been fully instantiated
# this operation must be linear w.r.t the size of the tree
# because we can't perform any efficient search
def path_to_root(root, target, path):
    if root is None:
        return False

    path.append(root)
    if root is target:
        # the path includes the node itself
        return True
    if path_to_root(root.left, target, path) or path_to_root(root.right, target, path):
        return True
    path.pop()
    return False



def lca(root, a, b):
    # we could do this more efficiently with one pass, but this is easier to code
    apath = []
    path_to_root(root, a, apath)

    bpath = []
    path_to_root(root, b, bpath)

    while apath[-1] is not bpath[-1]:
        if len(apath) > len(bpath):
            apath.pop()
        elif len(bpath) > len(apath):
            bpath.pop()
        else:
            apath.pop()
            bpath.pop()
    return apath[-1].data
