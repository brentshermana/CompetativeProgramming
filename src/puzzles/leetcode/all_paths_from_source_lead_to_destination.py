# I failed this problem because I was considering solutions with much higher runtime
# The takeaway here is that I could accomplish both my goals (finding leaf nodes
# and detecting cycles) using a unified DFS approach that still runs in linear time

# The problem statement is a little confusing but really just any cycle that's reachable from source
# indicates you should return false, because either:
#
# 1) the cycle contains destination, so the destination has outgoing edges
# 2) the cycle can reach destination, so there are infinite ways to reach destination
# 3) the cycle does not reach destination, so not all paths lead to destination

from collections import defaultdict

def helper(adj, dest, current, in_stack, visited):
    """
    A custom dfs that tracks two things:
    1) did we see any failure conditions (cycles or leaf nodes that aren't dest)
    2) did we see dest
    so we return a tuple with those two bools
    """
    if in_stack[current]:
        # fail condition due to cycle
        # note that we're checking this BEFORE the visited set,
        # otherwise this condition will never be met
        return (True, False)

    if visited[current]:
        # we only need to visit each node once to detect a cycle.
        #
        # without the visited set, runtime would be 2^N, as there are
        # order 2^N possible paths from a starting node
		# through a directed acyclic graph
        # (and if the graph is cyclic, the infinite paths don't matter
        #  because we'll detect the cycle and stop)
        return (False, False)

    visited[current] = True
    in_stack[current] = True

    # values we need to return
    fail = False
    saw_dest = current == dest

    if current not in adj:
        # leaf
        if current == dest:
            saw_dest = True
        else:
            fail = True
    else:
        for node in adj[current]:
            path_fail, path_saw_dest = helper(adj, dest, node, in_stack, visited)
            # add what we saw down this path to the result
            fail = fail or path_fail
            saw_dest = saw_dest or path_saw_dest

    in_stack[current] = False

    return fail, saw_dest


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # build the adjacency list
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)

        fail, saw_dest = helper(adj, destination, source, [False for _ in range(n)], [False for _ in range(n)])
        return saw_dest and not fail
