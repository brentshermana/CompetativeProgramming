# given two lists A and B
# B is an anagram of A
# - so, B is a random permutation of A
# produce an index mapping from A to B
# s.t. P[i] = j --> A[i]=B[j]
# the lists may contain duplicates. Any valid answer is fine,
# but we shouldn't map to the same index twice

from collections import defaultdict

class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        # linear space: map values in B to lists of indices where they occur
        # linear time: iterate through A and populate the mapping using
        #              those indices
        b2i = defaultdict(list)
        for i, n in enumerate(B):
            b2i[n].append(i)

        mapping = []
        for n in A:
            mapping.append(b2i[n].pop())

        return mapping
