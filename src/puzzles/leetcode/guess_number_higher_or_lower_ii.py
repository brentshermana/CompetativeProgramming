# This is a pretty straightforward problem to solve conceptually,
# but the implementation provides a lot of head scratching moments
# and opportunities for off-by-one
# indexing errors


from collections import defaultdict
import math
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = defaultdict(list)
        # handling edge cases: any interval of length 0 or 1 is 0
        # we ensure size=0 has an extra cell to continue the pattern that each higher level has one
        # less length
        dp[0] = [0 for _ in range(n+1)]
        dp[1] = [0 for _ in range(n)]
        for new_size in range(2, n+1):
            for start in range(n+1-new_size):
                best = math.inf
                for pivot in range(start, start+new_size):
                    left_size = pivot-start
                    left = dp[left_size][start]
                    # print("{} {} {} {}".format(new_size, left_size, pivot, start))
                    # print(dp)
                    right = dp[new_size-left_size-1][pivot+1]
                    best = min(best, max(left, right) + pivot+1)
                dp[new_size].append(best)
        return dp[n][0]
