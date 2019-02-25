# Subarray Sum Equals K
# Difficulty:Medium
#
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


# I have the right idea here, but I ran out of time!

class Solution:

    def valid_rng(self, rng):
        return rng[0] >= 0 \
            and rng[1] <= len(self.nums) \
            and rng[1] - rng[0] > 0

    def process(self, rng, sum):
        if rng not in self.dp and self.valid_rng(rng):
            self.dp[rng] = sum
            self.stack.append(rng)


    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        self.dp = dp = {}
        self.stack = stack = []
        self.nums = nums
        self.k = k

        stack.append( (0,1,) )
        dp[ (0,1,) ] = nums[0]

        while len(stack) > 0:
            cur = stack.pop()
            if cur[1] < len(nums):
                # extend
                self.process((cur[0], cur[1]+1,), nums[cur[1]+1])
            # truncate
            self.process((cur[0]+1, cur[1]+1,), -nums[cur[0]])

        return len(list(filter(lambda x: x[1] == k, dp.items())))

