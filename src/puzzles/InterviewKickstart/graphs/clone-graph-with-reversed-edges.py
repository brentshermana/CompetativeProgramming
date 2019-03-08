# the graph is strongly connect and directed.

# assume there will not be duplicate edges or edges connecting
# a node to itself

# each node contains distinct values in 1 ... n

# don't modify the given graph


# class Node:
#     def __init__(self):
#         self.val = 0
#         self.neighbours = []

from collections import defaultdict

def build_other_graph(node):
    # map the node value to the node
    nodes = defaultdict(Node)

    visited = set()

    # handles edge case of only one node by making sure it's
    # in the set
    nodes[node.val].val = node.val

    stack = [node]
    visited.add(node.val)
    while len(stack) > 0:
        n = stack.pop()
        for adj in n.neighbours:
            # add the reversed edges
            nodes[adj.val].neighbours.append(nodes[n.val])
            # add to the stack
            if adj.val not in visited:
                visited.add(adj.val)
                stack.append(adj)

    # never actually got around to setting the node copies'
    # 'val' attr
    for v, n in nodes.items():
        n.val = v

    return nodes[node.val]
