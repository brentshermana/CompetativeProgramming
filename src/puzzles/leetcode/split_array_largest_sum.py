# Not my solution, but it's much faster
# we avoid extra computation by arranging the subproblems to that you only
# need to consider ranges of the form [0, n)
# rather than every possible [i, j)

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if not nums or not m or len(nums) < m:
            return

        n = len(nums)
        # pre_sum[i] is the sum of elements [0, i)
        # (i not inclusive)
        #
        # we can get any range [i, j)
        # in constant time using pre_sum[j] - pre_sum[i]
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        # f[i]: the optimal minimal largest sum of the subarray [0, i)
        #       for the current level of array splits
        # * first cell refers to the subarray at the beginning of the array
        #   with zero splits
        f = [float("inf")] * (n + 1)
        # this cell refers to the range [0, 0), which is empty (sum = zero)
        f[0] = 0

        for total_splits in range(m):
            for i in range(n, 0, -1):
                # To compute f[i], we need to consider each possible new split point along [0, i)
                #
                # The only trick here is that if in the previous loop we computed all solutions
                # with (for example) three splits, we can ignore the first three possible
                # split points because otherwise we'd have at least one empty subarray, which
                # will never result in an optimal solution.
                #
                # You could start this loop at zero and get the same correct solution, but it would
                # be a little slower
                for split_point in range(total_splits, i):
                    # because we iterate from the highest i downward,
                    # f[split_point] always contains the value for the previous level
                    # of splits
                    #
                    # for any number of splits, we've already computed the solution for the previous number
                    # of splits, so we just need to add one additional split
                    #
                    # example:
                    #    total_splits = 3
                    #    i            = 10
                    #    split_point  = 4
                    #
                    # * f[split_point] is the value of the subproblem where m=3 for the range [0, split_point)
                    #   because we're computing a new subproblem m=4 for the range [0, i)
                    # * we use that subproblem, which has three of the splits, and add an additional
                    #   subarray [split_point, i). we use pre_sum to compute the sum of that new subarray
                    #   ( everything else has already been computed )
                    max_subarray_for_split = max(f[split_point], pre_sum[i] - pre_sum[split_point])
                    # min operation ensures we keep the optimal solution
                    f[i] = min(f[i], max_subarray_for_split)

        return f[n]


# MY ORIGINAL SOLUTION: SLOW

# perform 'm' splits to minimize the largest sum

# compute all split sums, and take the smallest 'm' non-overlapping ones?

# f(i, j, m): for the subarray i-j inclusive, what's the smallest split
#          array sum?
# f(i, j, 1) = sum(a[i:j+1]) <- base case
# ^^^ computing this naively is n^3, depending on how bad our overall solution is we may want
#     to optimize
# f(i, j, m) = min(f(i, k, 1), f(k+1, j, m-1) for k in i+1..j-1)
# ^^^ I don't see a better way to compute this than in linear time (j-i)
#
# bottom-up observation: we only ever need to keep around m=1 and the m before whatever we're currently computing!
#
# total time complexity: number of subarrays, which we iterate over to compute every level, times
#                        the number of levels
#                        so len(a)^2 * m

from collections import defaultdict
import math

class Solution:
    def splitArray(self, a: List[int], m: int) -> int:
        # m -> i,j -> val
        # we keep m separate to support removing a level once we're done with it
        dp = defaultdict(dict) # i, j, m

        # set up initial level
        for i in range(len(a)):
            for j in range(i, len(a)):
                # default value 0 handles j==i case
                dp[1][(i, j)] = dp[1].get((i, j-1), 0) + a[j]

        for n in range(2, m+1):
            for i in range(len(a)):
                for j in range(i, len(a)):
                    for k in range(i, j+1):
                        # technically these bounds cause us to consider some
                        # unnecessary situations like splitting a single element into two sections,
                        # where each section contains the element,
                        # but it makes the code a lot cleaner and will not result in the optimal
                        # solution anyways

                        # use a default value for k+1 .. j because that can be invalid (2, 1)
                        max_sum = max( dp[1][(i,k)], dp[n-1].get((k+1, j), math.inf) )
                        # use a default value here because on the first iteration this value
                        # doesn't exist yet
                        dp[n][(i, j)] = min(max_sum, dp[n].get((i,j), math.inf))
        return dp[m][(0, len(a)-1)]
