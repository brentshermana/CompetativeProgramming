class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class RangeIter:
    """
    We could write this class as a generator instead, but this is harder!

    This is an "inclusive" range iter, so it will include the lo and hi nodes
    if they exist, but nothing above or below them
    """
    def __init__(self, root, lo, hi):
        # each element on the stack is (node, should_explore_left)
        # we need the bool to remember what we've already done with a node!
        self.stack = [(root, True)]
        self.lo = lo
        self.hi = hi


    def __iter__(self):
        return self

    def __next__(self):
        while len(self.stack) > 0:
            n, explore_left = self.stack.pop()

            # None check simplifies the following logic
            if n is None:
                continue

            if explore_left:
                # mark the current node as having branched left
                self.stack.append( (n, False) )
                # process left child before reprocessing
                self.stack.append( (n.left, True) )
            else:
                # we have already processed everything that's less than this node already
                # the only things remaining are this node, and then the right subtree
                # in that order
                if n.val < self.lo:
                    # explore right later
                    self.stack.append( (n.right, True) )
                elif n.val <= self.hi:
                    # explore right later
                    self.stack.append( (n.right, True) )
                    # n is in the range!
                    return n
                else:
                    # we're too far to the right! don't go any further
                    pass
        # out of work to do
        raise StopIteration


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        n = self.root
        while True:
            if n.val < val:
                if n.right:
                    n = n.right
                else:
                    n.right = Node(val)
                    return
            else:
                if n.left:
                    n = n.left
                else:
                    n.left = Node(val)
                    return

    def next_highest(self, val):
        """
        return the node whose value is the closest to but greater than val
        this is equivalent to an inorder successor
        """
        if self.root is None:
            return None
        # NOTE: stack is NOT NEEDED because we never need to search more than one path!
        n = self.root
        ret = None
        while n is not None:
            if n.val > val:
                # the current node may be the closest to 'val' that's also above val
                #
                # it's also possible that a better option exists in the left subtree
                #
                # we perform an assign now. If we don't find anything else, this will be returned.
                #
                # note that no comparison to the prev 'ret' val is needed because we'll never see a
                # node with a higher value than the prev 'ret' val -- that's what delving into
                # the left subtree means!!!
                ret = n
                n = n.left
            else:
                n = n.right
        return ret


class NodeWithParent:
    def __init__(self, val, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.val = val

class TreeWithParent:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = NodeWithParent(val, None)
            return

        n = self.root
        while True:
            if n.val > val:
                if n.left:
                    n = n.left
                else:
                    n.left = NodeWithParent(val, n)
                    return
            else:
                if n.right:
                    n = n.right
                else:
                    n.right = NodeWithParent(val, n)
                    return

    def get(self, val):
        n = self.root
        while n is not None and n.val != val:
            if n.val > val:
                n = n.left
            else:
                n = n.right
        return n

    def next_highest(self, node):
        """
        return the smallest node that's larger than the input node, or None
        if no such value exists
        """
        if node.right is not None:
            # find smallest node in right subtree
            #
            # why does this work? let's consider the possible cases:
            # 1) node is the right subtree of its parent:
            #    the parent's value (and everything attached to it) is too low to be a candidate!
            # 2) node is the left subtree of its parent:
            #    the parent is greater than 'node', but also greater than any values in the right
            #    subtree of 'node', one of which would be the correct return val of this function!
            n = node.right
            while n.left is not None:
                n = n.left
            return n
        else:
            # move up until 'node' is a LEFT SUBTREE to its parent. that parent is the first node
            # up the chain with a larger value.
            while node.parent is not None and node.parent.left is not node:
                node = node.parent

            # note that parent could be None here...
            #
            # this parent is always going to be the solution!
            # * its parent will either be larger than it or smaller than the original input node
            # * its right subtree will be larger than it
            return node.parent
