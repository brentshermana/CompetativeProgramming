
# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]




# I'm trying to implement the general approach suugested here:
# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# (although I haven't looked at the exact solution for this problem)

# consider:
# - where to add to all_sets? When a set is full
# - difference from subset solutions: each digit needs to be placed in each position
#   - rather than passing along a start_index, keep track of all the valid indices
#     that haven't been added yet

# in order to support efficient operation on this "candidates" list, we're going to want a DLL?
# .... no, a deque works just fine and Python gives us one already!

# SUCCESS in the end this solution did basically the same as my solution for permutations II,
# but it's helped me internalize this framework somewhat

from collections import deque

def backtrack(all_sets, temp_set, candidates):
    if len(candidates) == 0:
        # we only need to perform the actual copying once, when the temp_set is full!
        all_sets.append(list(temp_set))
    else:
        for _ in range(len(candidates)):
            # take a candidate and put it at the front of the set
            candidate = candidates.popleft()
            temp_set.append(candidate)

            # add all permutations formed with 'candidate' in front
            backtrack(all_sets, temp_set, candidates)

            # put that candidate at the back of the list, exposing a new
            # one at the front
            temp_set.pop()
            candidates.append(candidate)


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        candidates = deque(nums)
        all_sets = []
        backtrack(all_sets, [], candidates)
        return all_sets
