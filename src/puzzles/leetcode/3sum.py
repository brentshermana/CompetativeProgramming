# You can build the more complicated solution (3sum) from a subroutine (2sum)!
# This also makes preventing duplicates easier!

def shift(a, i, direction):
    """helper for skipping dupes"""
    orig = a[i]
    while i >= 0 and i < len(a) and a[i] == orig:
        i += direction
    return i

def two_sum(a, target):
    results = []
    left = 0
    right = len(a)-1
    while left < right:
        val = a[left] + a[right]
        if val == target:
            results.append([a[left], a[right]])
            left = shift(a, left, 1)
            right = shift(a, right, -1)
        elif val < target:
            left = shift(a, left, 1)
        else:
            right = shift(a, right, -1)
    return results

class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        a.sort()
        results = []
        i = 0
        while i < len(a):
            for x, y in two_sum(a[i+1:], -a[i]):
                results.append([a[i], x, y])
            i = shift(a, i, 1)
        return results
