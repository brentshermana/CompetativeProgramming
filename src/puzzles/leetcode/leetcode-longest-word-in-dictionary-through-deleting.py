# SUCCESS
# the key here was observing that we can determine if a -> b through deletions with a simple linear pass,
# basically checking if b is a subsequence of a
# my sort causes len(s)*n + nlogn runtime, even

def delmatch(a, b):
    if len(b) > len(a):
        # save the cost of list copy
        return False
    a = list(a)
    b = list(b)
    while len(a) >= len(b) > 0:
        if a[-1] == b[-1]:
            a.pop()
            b.pop()
        else:
            a.pop()
    return len(b) == 0 # otherwise some characters in b weren't matched
    
class Solution:
    def findLongestWord(self, s: 'str', d: 'List[str]') -> 'str':
        longest = ""
        while len(d) > 0:
            temp = d.pop()
            if len(temp) < len(longest):
                continue
            if len(temp) == len(longest) and temp >= longest:
                # if they're the same length, the new string
                # needs to be less than the current one
                continue
            if delmatch(s, temp):
                longest = temp
        return longest