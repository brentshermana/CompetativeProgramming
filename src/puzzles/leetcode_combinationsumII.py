# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]


# SUCCESS by following the same framework described in leetcode_permutations.py, among others.
# The main thing to recognize is that you shouldn't create a new fork with candidates[i]
# in the temp set if you've already done that on the given fork, because that will create
# duplicate sets.

def backtrack(all_sets, temp_set, temp_sum, target_sum, candidates, start_i):
    if temp_sum == target_sum:
        all_sets.append(list(temp_set))
    elif temp_sum < target_sum:
        for i in range(start_i, len(candidates)):
            # we need to prevent duplicate sets in the case that
            # a digit occurs twice or more in 'candidates'
            if i > start_i and candidates[i-1] == candidates[i]:
                # backtrack() has already been called with temp_sets
                # containing value candidates[i], so we should skip this
                continue
            else:
                temp_set.append(candidates[i])
                # create a 'fork' that contains the candidate.
                # This ongoing loop will maintain the set that doesn't contain it
                backtrack(all_sets, temp_set, temp_sum+candidates[i], target_sum, candidates, i+1)
                temp_set.pop()

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        print("Candidates {}".format(candidates))
        all_sets = []
        backtrack(all_sets, [], 0, target, candidates, 0)
        return all_sets
