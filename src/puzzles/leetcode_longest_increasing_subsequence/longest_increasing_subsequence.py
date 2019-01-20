# FAILED. Here is someone else's solution from Leetcode:
#
# 1: Dynamic Programming (N^2)
#   DP is an array such that there's one element for each element in the
#   given number array. Each cell contains a number corresponding to the length
#   of the subsequence containing and ending with that number
#   (obviously, they all start at 1)
#
#   Algorithm:
#       for each position i,
#           for each position j s.t. j < i AND nums[j] < nums[i]
#               dp[i] = max(dp[j]) + 1
#
#   The core idea here is to incrementally build up subsequence lengths
#   By considering existing sequences (built up from the lhs) and choosing
#   to connect each tail/end with the longest candidate subsequence
#
#
# 2: Build up subsequence using Binary Search (n log(n))
# Idea: each element we see is either going to be the biggest of our
# existing subsequence (put it at the end), or smaller than some existing
# element of our subsequence (replace it).
#
# This works because we are always going to prefer smaller numbers to bigger
# ones. For example, in the problem [1, 4, 3, 5], [1 3 5] is preferable to [1 4 5].
#
# The primary implementation detail is creating a custom binary search which
# will always return the correct index to perform the replacement at


class Solution(object):

#using dP
def lengthOfLIS1(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    dp = [1]*len(nums)
    for i in range (1, len(nums)):
        for j in range(i):
            if nums[i] >nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

#using binary search
def lengthOfLIS(self, nums):
    def search(temp, left, right, target):
        if left == right:
            return left
        mid = left+(right-left)/2
        return search(temp, mid+1, right, target) if temp[mid]<target else search(temp, left, mid, target)
    temp = []
    for num in nums:
        pos = search(temp, 0, len(temp), num)
        if pos >=len(temp):
            temp.append(num)
        else:
            temp[pos]=num
    return len(temp)