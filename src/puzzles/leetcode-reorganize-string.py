# I didn't get this myself... had to look at the answer

# I got caught up in the logic regarding how to merge the string together,
# where my logic could have been correct but was also overly complicated, involving
# heaps and queues and maps and stuff

from collections import defaultdict
from heapq import heappush, heappop, heapify
class Solution:
    def reorganizeString(self, S: 'str') -> 'str':
        counts = defaultdict(int)
        for c in S:
            counts[c] += 1
            
        if max(counts.values()) > (len(S)+1) // 2:
            return ''
        
        # we reverse the sign of the count so that a min heap works
        heap = [(-v, k) for k, v in counts.items()]
        heapify(heap)
        
        s = ""
        while len(heap) > 0:
            neg_count, char = heappop(heap)
            if len(s) > 0 and s[-1] == char:
                nc, c = heappop(heap)
                heappush(heap, (neg_count, char))
                neg_count, char = nc, c
            s += char
            neg_count += 1
            if neg_count < 0:
                heappush(heap, (neg_count, char))
        return s