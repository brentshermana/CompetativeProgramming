# Given a set of candidate numbers (candidates) (without duplicates)
# and a target number (target), find all unique combinations in candidates
# where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]





# The fact that the same number can be used multiple times is a big deal, and 
# significantly impacts how the problem must be approached. Space complexity 
# will be important here.

# in the worst case scenario, our target will be T, and our candidates will be [1 ... T].
# so, the first solution will be  [1] * T,
# the second solution will be [1] * T-2 + [2], and so on.
#
# in general, we can describe the number of solutions to T as being the sum of
# **Subproblem(T-N)**, summed over each unique N <= T. We can precompute these subproblems
# LAZILY (as we won't necessarily need all of them)
#  ^^^ observation: this problem lends itself to recursion
# Brute force approach where we don't save subproblems is
# x(n) = x(n-1) + x(n-2) + ... + x(1)
#  ^^^ we will compute x(n-1) twice, x(n-2) four times, etc. ...
# so the worst case is 2^N







# Success! At first I had some trouble getting duplicate sets
# eg [2, 2, 3], [2, 3, 2], [3, 2, 2]
# but I was able to prevent that by iterating through each candidate number instead.
# So for candidate 2 and target 9, I would add [2], [2, 2], through [2, 2, 2, 2]
# and any sets I could create using these sets and already existing sets, which would
# be necessarily composed of numbers besides 2
#   HOWEVER other people came up with better solutions by exploiting the observation that
#   you can pass a subset of the candidates to recursive calls:
# class Solution:
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         if target == 0:
#             return [[]]
#         result = []
#         for i in range(len(candidates)):
#             c = candidates[i]
#             if c <= target:
#                 tail = self.combinationSum(candidates[i:], target - c)
#                 for row in tail:
#                     result.append([c] + row)
#         return result



import copy
from collections import defaultdict

class Solution:

    def _combinationSum(self, candidates, target, dp):
        for c in candidates:
            if c > target:
                break
            else:
                # do work: process this candidate
                # (this is the only time we will add this number into sets,
                # ensuring there are no duplicate sets)
                product = c
                product_set = [c]
                while product <= target:
                    # add the product_set
                    dp[product].append(copy.copy(product_set))

                    # create other valid sets
                    for other_set_sum in range(1, target-product +1):
                        for other_set in dp[other_set_sum]:
                            # verify that other_set isn't just another product_set containing this number
                            if other_set[-1] != c:
                                dp[product + other_set_sum].append(copy.copy(other_set) + copy.copy(product_set))

                    product += c
                    product_set.append(c)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # # for now we'll assume candidates is sorted, as that has held true
        # # for the first examples
        candidates.sort()

        dp = defaultdict(list)
        self._combinationSum(candidates, target, dp)
        return dp[target]
        
# What are we doing wrong here? Getting multiple permutations of the same solution set:

# call 7:
#     call 5:
#         call 3:
#             return [3]
#         call 2:
#             return [2]
#         return [2,3], [3, 2]
#     return 

#     call 4:
#         call 2:
#             return [2]
#         return [2, 2]
#     return [3, 2, 2]

# so clearly there's duplication, but what's the core problem?
# We should really only process each candidate number once, because
# we can add a candidate number any number of times!
