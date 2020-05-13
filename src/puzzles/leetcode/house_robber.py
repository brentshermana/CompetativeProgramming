# recursive formulation: r[i] = max(a[i] + r[i+2], r[i+1] )
# put in reverse for easier iteration:
#                        r[i] = max(a[i] + r[i-2], r[i-1])
# base case: r[x] for x < 0: 0

class Solution:
    def rob(self, nums: List[int]) -> int:
        # only need to keep the last two vals, which when we start are both the base case
        pred1 = 0
        pred2 = 0
        for n in nums:
            current = max(n+pred2, pred1)
            pred2 = pred1
            pred1 = current
        return pred1
