# HARD. I seem to have some trouble with array problems because the data structure
#       is so stupidly simple that most of the work goes into tedious counting and
#       and iteration


# My solution. it works, but it seems to take a lot of code and isn't very clean

# it's never useful to consider windows that don't have all the chars. greedy strategy:
# * starting from the start, expand right until you have all the chars
# * contract from the left as much as you can while still retaining all the chars
# * repeatedly extend by one space then contract until the end is reached

import math

def contract(start, end, s, d):
    while start < end:
        if s[start] not in d:
            start += 1
        else:
            if d[s[start]] > 0:
                d[s[start]] -= 1
                start += 1
            else:
                break
    return start

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        't' is NOT a set. there can be duplicates in t, and each char must exist in our window
        at least as many times as it exists in t
        """

        # the keys will be the characters we care about
        # when the val for the key is zero, we have enough of that char. higher values
        # indicate surplus
        d = {}
        for c in t:
            d[c] = d.get(c, 0) - 1

        start = 0
        end = 0

        # first, extend until we have all chars
        missing_chars = len(d)
        while end < len(s) and missing_chars > 0:
            if s[end] in d:
                d[s[end]] += 1
                if d[s[end]] == 0:
                    missing_chars -= 1
            end += 1

        if missing_chars > 0:
            return ""

        start = contract(start, end, s, d)
        best_window = s[start:end]

        # repeatedly extend by one, contract, see if we find a better solution
        while end < len(s):
            if s[end] in d:
                d[s[end]] += 1
            end += 1

            start = contract(start, end, s, d)
            if end-start < len(best_window):
                best_window = s[start:end]

        return best_window
