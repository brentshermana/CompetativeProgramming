# print all root->leaf paths, one per line

def rec(root, path):
    path.append(str(root.val))
    children = [c for c in (root.left_ptr, root.right_ptr) if c is not None]
    if len(children) == 0:
        print(' '.join(path))
    else:
        for child in children:
            rec(child, path)
    path.pop()

def printAllPaths(root):
    if root is not None:
        rec(root, [])
