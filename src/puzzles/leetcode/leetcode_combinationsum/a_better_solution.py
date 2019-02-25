class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0:
            return [[]]
        result = []
        for i in range(len(candidates)):
            c = candidates[i]
            if c <= target:
                tail = self.combinationSum(candidates[i:], target - c)
                for row in tail:
                    result.append([c] + row)
        return result