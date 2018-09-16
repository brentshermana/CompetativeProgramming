# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
#
# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.
#
# According to the example above:
#
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

# SOLVED, but after time ran out.
#
# the first thing that must be understood is that the division rules define ratios between variables,
# and those variables are transitive. so, ratio(a, c) = ratio(a,b) * ratio(b,c).
# also, ratio(a,b) = 1/ratio(b,a)
#
# so these ratio definitions are essentially connections in the graph. Finding the ratio between
# two nodes is equivalent to finding the path between them. I arbitrarily chose DFS because it
# has a lower memory overhead
#
# my first idea was to precompute the "fully connected" version of the graph first, but that turned out
# to be unfeasible for my approach. Someone else adapted Floyd Warshall to accomplish this:
# https://leetcode.com/problems/evaluate-division/discuss/88175/9-lines-%2522FloydWarshall%2522-in-Python/150944
# I should read up on the more advanced graph algorithms...

from collections import defaultdict as dd

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        ratios = {}  # {(a,b):k, ...}
        neighbors = dd(set)  # {a: set(b), b: set(a), ...}

        for eq, v in zip(equations, values):
            a, b = eq[0], eq[1]

            ratios[(a, a)] = float(1)
            ratios[(b, b)] = float(1)

            # connect a and b
            neighbors[a].add(b)
            neighbors[b].add(a)
            ratios[(a, b)] = v
            ratios[(b, a)] = 1 / v

            # # connect other neighbors of a to b, other neighbors of b to a
            # for x, y in zip([a,b],[b,a]):
            #     for n in neighbors[x]:
            #         if n == x or n == y: continue
            #         if (n,y) not in ratios: # n is connected to a but not b
            #             neighbors[n].add(y)
            #             neighbors[y].add(n)
            #             ratios[(y,n)] = ratios[(y,x)] * ratios[(x,n)]
            #             ratios[(n,y)] = 1/ratios[(y,n)]

        # for pair, ratio in ratios.items():
        #     print("{} -> {}".format(pair, ratio))
        ret = []
        for a, b in queries:
            if a not in neighbors or b not in neighbors:
                ret.append(float(-1))
                continue

            # dfs setup:
            visited = set()
            stack = [(a, float(1))]
            visited.add(a)
            success = False
            while len(stack) > 0 and not success:
                x, r = stack.pop()
                if x == b:
                    ret.append(r)
                    success = True
                else:
                    for n in neighbors[x]:
                        if n not in visited:
                            visited.add(n)
                            stack.append((n, r * ratios[(x, n)]))
            if not success:
                ret.append(float(-1))
        return ret
