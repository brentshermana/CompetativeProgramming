# I was able to solve this in n^2 time using a modified trie,
# but it seems like there are much more optimal solutions
# in the leetcode discussion for this problem

import math

# N^2
def buildTrie(s, i, prev):
    """
    This trie allows you to pass through
    the longest possible subsequence
    in linear time,
    but requires n^2 time to construct
    """
    if i == len(s):
        return
    current = {}
    for p in prev:
        # important for handling duplicate chars!
        # keep the edge to the foremost node, because
        # if we have to skip chars that can always
        # happen later, but we can never go backwards!
        if s[i] not in p:
            p[s[i]] = current
    prev.append(current)
    buildTrie(s, i+1, prev)


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        root = {}
        buildTrie(source, 0, [root])
        subsequences = 0
        i = 0
        while i < len(target):
            subsequences += 1
            # greedily match as much of target as you can for this subsequence
            current = root
            while i < len(target) and target[i] in current:
                current = current[target[i]]
                i += 1
            # if we didn't match anything there's no solution
            if current is root:
                return -1
        return subsequences
