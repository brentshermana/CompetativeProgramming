# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
#
# Example 1:
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
#     After flipping, the maximum number of consecutive 1s is 4.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
#
# Follow up:
# What if the input numbers come in one by one as an infinite stream?
# In other words, you can't store all numbers coming from the stream
# as it's too large to hold in memory. Could you solve it efficiently?


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lz = -1  # last zero seen
        base = 0
        cap = 0

        largest = 0

        while cap < len(nums):
            if nums[cap] == 0:
                if lz < base:  # seeing first zero in array, that's fine
                    lz = cap
                else:
                    base = lz + 1
                    lz = cap
            cap += 1

            # finally, update the max
            largest = max(cap - base, largest)

        return largest