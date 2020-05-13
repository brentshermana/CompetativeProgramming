# NOT my solution, mine was trivial with a set

# most members of the input array exist twice. return the element that is contained
# only once


# bit manipulation: xor is associative, so xor-ing the list in whatever order
# it's in is equivalent to xor-ing the numbers in sorted order
# a xor a is zero
# a xor a xor b is b
# a xor a xor b xor b xor c is c
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
