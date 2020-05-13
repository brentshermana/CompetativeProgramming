# This problem is interesting primarily because it looks like a DP problem, but was much-
# more easily solved using heaps while still beating 97%

# largest possible sum for subset meeting constraints:
# * size <= the size limit
# * multiple items can have the same label, and there's a limit on the number values in the subset that share a label
#
# brute force: generate all possible subsets while enforcing the constraints: 2^N
#
# we can probably also formulate this in a DP format, but the 'state' will be complicated because has to be encoded as well!
#
#
# example: a:1 a:2 b:1   setsize_limit = 2, keyshare_limit=1
# * state variable 1: the index we've processed up to (inclusive)
# * state variable 2: the number of elements currently in the set
# * state variable 3: the number of elements currently in the set FOR EACH KEY
#


# we can remove the keyshare_limit constraint by doing a first pass over the input data and retaining the top N vals of each key!!!!
# that makes things easier

# without that constraint, we just need to find the max sum of a particular size
# * approach 1: use another heap?
# * approach 2: use DP?
#   f[i, j] = max(f[i-1, j], f[i-1, j-1] + a[j])
#   and that would have to be done for each possible size at each index

from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], max_size: int, key_use_limit: int) -> int:
        vals_bykey = defaultdict(list)
        for label, val in zip(labels, values):
            heappush(vals_bykey[label], val)
            if len(vals_bykey[label]) > key_use_limit:
                heappop(vals_bykey[label])

        h = []
        for vals in vals_bykey.values():
            for val in vals:
                heappush(h, val)
                if len(h) > max_size:
                    heappop(h)
        return sum(h)
