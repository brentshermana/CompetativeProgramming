# Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.
#
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.

# SOLVED: unlike normal binary search, in this case you need to reason based on
# the index of the left element of the pair that you're currently looking at.
# because indices start at zero, if the singleton is to the right, your index
# will be even. if the singleton is to the left, your index will be odd

class Solution:
    def singleNonDuplicate(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """

        def valid_i(a, i, li, hi):
            return i >= 0 and i < len(a) and i >= li and i < hi

        def new_bounds(li, hi, lp, hp):
            if lp % 2 == 1:  # odd: singleton to left
                return (li, lp)
            else:  # even: singleton to right
                return (hp + 1, hi)

        def bs(a, li, hi): # low index, high index
            mi = (hi + li) // 2 # middle index

            if valid_i(a, mi - 1, li, hi) and a[mi - 1] == a[mi]:
                li, hi = new_bounds(li, hi, mi - 1, mi)
                return bs(a, li, hi)
            elif valid_i(a, mi + 1, li, hi) and a[mi + 1] == a[mi]:
                li, hi = new_bounds(li, hi, mi, mi + 1)
                return bs(a, li, hi)
            else:
                return a[mi]

        return bs(a, 0, len(a))