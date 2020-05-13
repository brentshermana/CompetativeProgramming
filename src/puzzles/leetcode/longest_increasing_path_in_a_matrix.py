# I'm including this problem because it was interesting to tackle using bottom-up
# HOWEVER, the memoization solution has a better time complexity because it avoids
# the sort operation

# This sounds like a DP problem!
# How do we build up subproblems?

# if the array were 1d, I'd just maintain the following:
# f(i) = max( f(i-1)+1 if f(i) > f(i-1),
#             f(i+1)+1 if f(i) > f(i+1),
#             1 otherwise)
#
# so it's pretty easy to build up solutions recursively, so a memo table is also easy
# how can we do this bottom-up (or equivalent?)
# go through nodes in order of increasing value! a node's longest path can never be overridden
# when a node of higher or equal value is updated (which would force us to do more work)!

from collections import defaultdict

def adj(i, j, matrix):
    for k, l in ( (i+1, j), (i-1, j), (i, j+1), (i, j-1) ):
        if k >= 0 and l >= 0 and k < len(matrix) and l < len(matrix[0]):
            yield k, l

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        # map value to locations where value exists
        d = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                d[matrix[i][j]].append( (i,j) )

        best = 1
        dp = []
        for _ in matrix:
            dp.append([1] * len(matrix[0]))

        for val, locations in sorted(d.items(), key=lambda x: x[0]):
            for i, j in locations:
                for k, l in adj(i,j,matrix):
                    if matrix[k][l] < matrix[i][j]:
                        dp[i][j] = max(dp[i][j], dp[k][l]+1)
                best = max(best, dp[i][j])
        return best
