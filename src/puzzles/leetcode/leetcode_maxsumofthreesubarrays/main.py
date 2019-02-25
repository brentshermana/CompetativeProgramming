# Maximum Sum of 3 Non-Overlapping Subarrays
# Difficulty:Hard
#
# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
#
# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.
#
# Example:
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
# Note:
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).


# This was tough! my solution works, but is n^3, which is really bad.
# I was considering a local search-like solution, but didn't think that would work in the
# general case. For example, consider this case in the simplified scenario where we pick two
# subsequences instead of three:
# nums =  1 1 1 1 5 8 9 6 1 1 1
# in this situation, if we greedily 'take' one subsequence, that would be 8 and 9. 5 and 6 are
# both still large numbers, but our second subsequence can only take one of them!

# as it turns out, there are other solutions, including one which runs in linear time.
# That's also in this directory.
#
# limitations in my thinking about this problem included not knowing how to structure the problem
# into a dynamic programming solution, and limiting myself by not considering other looping
# patterns other than the 'standard' selection sort style

def subseqSums(nums, k):
    cur_sum = sum(nums[:k])
    sums = [cur_sum]

    for i in range(k, len(nums)):
        cur_sum -= nums[i-k]
        cur_sum += nums[i]

        sums.append(cur_sum)

    return sums

class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sums = subseqSums(nums, k)

        print(sums)

        best = None
        best_score = -1

        for i in range(0, len(sums)-2*k):
            for j in range(i+k, len(sums)-k):
                for p in range(j+k, len(sums)):
                    tmp = sums[i] + sums[j] + sums[p]
                    if tmp > best_score:
                        best_score = tmp
                        best = [i,j,p]

        return best
