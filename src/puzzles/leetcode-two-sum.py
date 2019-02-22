from heapq import heappush, heappop, heapify

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        minh = [(n, i) for i, n in enumerate(nums)]
        # we also negate the index for maxh so that we get the highest index for a given element
        maxh = [(-n, -i) for i, n in enumerate(nums)]
        heapify(minh)
        heapify(maxh)
        while minh[0][0] + -maxh[0][0] != target:
            if minh[0][0] + -maxh[0][0] > target:
                heappop(maxh)
            else:
                heappop(minh)
        return [minh[0][1], -maxh[0][1]]
