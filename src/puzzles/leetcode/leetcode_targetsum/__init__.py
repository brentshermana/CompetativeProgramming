# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.

# SOLVED.
# this is a dynamic programming problem, because the solution to a problem is constructed using subproblems,
# and those subproblems will frequently overlap.
# for example, take the problem [1,1,1,1] 3. It delegates to [1,1,1] 4 and [1,1,1] 2. Both of those subproblems
# have a subproblem in common, [1,1] 3 (which is zero)
# by storing these subproblems, we are frequently able to halve the size of the problem space

# This solution from Leetcode takes the same idea, but takes a bottom-up approach, which is more efficient
# than my solution because it avoids copying and storing a bunch of different tuples. instead, it just maps
# target values to the number of ways to represent them, beginning from one way to represent zero.
#
# Also notice that because 'm' replaces 'memo' after each iteration through the dictionary, we're only tracking
# The last 'tier': The set of subproblems that are of size 'current_problem_size' - 1. That also introduces
# savings on space.
#
# class Solution(object):
#     def findTargetSumWays(self, nums, S):
#         from collections import defaultdict
#         memo = {0: 1}
#         for x in nums:
#             m = defaultdict(int)
#             for s, n in memo.iteritems():
#                 m[s + x] += n
#                 m[s - x] += n
#             memo = m
#         return memo[S]



class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def fill(dp, nums, target):
            k = (nums, target)
            if len(nums) == 1:
                ret = 0
                if nums[0] == target: ret += 1
                if -nums[0] == target: ret += 1
                return ret
            if k in dp:
                return dp[k]
            else:
                new_nums = nums[1:]
                ret = fill(dp, new_nums, target + nums[0]) + fill(dp, new_nums, target - nums[0])
                dp[k] = ret
                return ret

        return fill({}, tuple(nums), S)