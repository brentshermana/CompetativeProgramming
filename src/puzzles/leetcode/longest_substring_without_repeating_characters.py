# formulation:
# f[i] = min(f[i-1]+1, i-index_of_prev[a[i]] )
# basically we're appending a char to the current substring if the substring doesn't contain that
# char, otherwise we're truncating the substring down to just after the last occurrence of the char

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we only ever need to hold the prev value
        current = 0
        best = 0
        index_of_prev = {}
        for i, c in enumerate(s):
            # we can also reduce space usage by removing elements from index_of_prev when
            # i-index_of_prev > current
            # basically it's only ever important if it's less than current+1, otherwise
            # it doesn't matter how much larger it is
            current = min(current+1, i-index_of_prev.get(c, -1))
            best = max(best, current)
            index_of_prev[c] = i
        return best
