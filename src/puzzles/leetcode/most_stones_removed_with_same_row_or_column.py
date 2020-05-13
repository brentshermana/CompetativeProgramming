# This was difficult!!!

# My original solution involved "simulating" the removal of stones,
# in an attempt to perform the maximal possible amount of removals
# I observed that you can always remove a node that only has one
# other node on the same row or col, and attempted to construct
# a greedy algorithm that could perform optimally
# That was bad


# Solution 1: use DFS to find connected components
# * It's essential to observe that this problem reduces down
#   to counting the number of connected components! Any
#   connected component can be reduced down to one stone
#   through optimal play
# * Note: it's not necessary to simulate said play, but it it were:
#   you could just repeatedly remove leaves from the spanning tree
#   which could also be constructed through DFS
#
# Solution 2: use Union-find to find the number of connected components
# That's what I used because I wanted to brush up on that algorithm,
# but I think it actually ends up being slower


import itertools

def find(parent, x):
    if parent[x] == -1:
        # x is the root
        return x
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[x_root] = y_root

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        on_row = defaultdict(list)
        on_col = defaultdict(list)
        # build up graph
        for i, (r, c) in enumerate(stones):
            on_row[r].append(i)
            on_col[c].append(i)

        # construct unions
        parent = [-1 for _ in range(len(stones))]
        for a in itertools.chain(on_row.values(), on_col.values()):
            # it's sufficient to union each pair
            for i in range(len(a)-1):
                union(parent, a[i], a[i+1])

        # Each disjoint set (not connected to another set)
        # can be reduced down to one node. We could simulate
        # that, but that's not the goal of the problem
        #
        # so, there are removals equal to the total number of nodes
        # minus those that remain at the end
        return len(parent) - parent.count(-1)
