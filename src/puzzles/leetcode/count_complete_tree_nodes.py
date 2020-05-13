# Tree problems that require lots of log / pow math take a long time for me, I
# need to practice more!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# the challenge is: how can we get to the rightmost node on the last level in logn time?
# and how do we know which position it's in?

# can we do an initial search along the left side to get the maximum depth, then binary search for
# the rightmost node along that depth?
# each search: o(lg(n))
# number of searches: o(lg(n/2))
# time complexity: lg(n) ** 2

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # need to check far left to get max depth:
        depth = 0
        n = root
        while n:
            n = n.left
            depth += 1

        if depth == 0:
            # edge case: depth==0 results in invalid results
            return 0

        # now, binary search along final row to get rightmost node
        base = 1
        lastrowlen = 2 ** (depth-1)
        cap = lastrowlen
        rightmost = 0
        while base < cap:
            mid = base + (cap-base)//2

            # perform the search
            # we want to "write off" (be left of) 'mid' nodes
            to_write_off = mid
            write_off = lastrowlen
            d = 0
            n = root
            while n is not None and d < depth:
                write_off //= 2
                d += 1
                if write_off <= to_write_off:
                    to_write_off -= write_off
                    n = n.right
                else:
                    n = n.left

            # search is complete, adjust bounds based on result
            if d < depth:
                # couldn't find that position
                cap = mid
            else:
                # found it!
                base = mid+1
                rightmost = max(rightmost, mid)

        # 'rightmost' is the highest index in the last row,
        # but we want to return the size of the tree
        rest_of_tree = 2**(depth-1) -1
        lastrow = rightmost+1
        return rest_of_tree + lastrow
