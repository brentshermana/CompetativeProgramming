from collections import deque

# the number of permutations is, mathematically, n factorial
# in addition to that, it takes 'n' amount of work to create each
# permutation, so the time complexity is n*(n!)


# I remember there being a general pattern that I picked up at Interview
# Kickstart (or leetcode?) that was a good general purpose solution
# that adapts well to a lot of these 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        deq = deque(nums)
        return self.inner_permute(deq)

    def inner_permute(self, deq):
        # base case
        if len(deq) == 0:
            return [[]]

        result = []
        for _ in range(len(deq)):
            x = deq.pop()
            for inner_result in self.inner_permute(deq):
                inner_result.append(x)
                result.append(inner_result)
            deq.appendleft(x)
        # after completing all operations, deq is unchanged from when it was called (important because callers rely on that!)
        return result
