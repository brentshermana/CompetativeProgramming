# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None

# approach: use an in-order iterator on each tree to sort the values into an array of nodes.
# Use that array to create a balanced tree, similarly to binary search

# for the iterators, I could use a generator function, but that would be too trivial.
# This is a good exercise. I wonder if there's a good way of doing this without the extra state?
class TreeIterator:
    def __init__(self, root):
        # state 0: just added
        if root is not None:
            self.stack = [(root, 0)]
        else:
            self.stack = []

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.stack) > 0:
            tmp, state = self.stack.pop()

            # left
            if state == 0:
                state += 1
                if tmp.left is not None:
                    self.stack.append((tmp, state))
                    self.stack.append((tmp.left, 0))
                    continue
            # self
            if state == 1:
                state += 1
                self.stack.append((tmp, state))
                return tmp.key
            # right
            if state == 2:
                if tmp.right is not None:
                    # we don't need tmp any more
                    self.stack.append((tmp.right, 0))
        # out of stuff
        return None

def construct_tree(nodes, base, cap):
    if base >= cap: # invalid range
        return None
    mid = (base + cap) // 2
    nodes[mid].left = construct_tree(nodes, base, mid)
    nodes[mid].right = construct_tree(nodes, mid+1, cap)
    return nodes[mid]


# Complete this function and return root of the BST
def mergeTwoBSTs(root1, root2):
    it1 = TreeIterator(root1)
    it2 = TreeIterator(root2)
    nodes = [] # sorted list of nodes

    a, b = next(it1), next(it2)
    while a is not None or b is not None:
        if b is None or (a is not None and a <= b):
            nodes.append(Node(a))
            a = next(it1)
        else:
            nodes.append(Node(b))
            b = next(it2)

    # now that we have a sorted list of nodes, connect them using binary search
    return construct_tree(nodes, 0, len(nodes))
