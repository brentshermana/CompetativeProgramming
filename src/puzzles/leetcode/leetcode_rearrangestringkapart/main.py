# Rearrange String k Distance Apart
# Difficulty:Hard
#
# Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.
#
# All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".
#
# Example 1:
# s = "aabbcc", k = 3
#
# Result: "abcabc"
#
# The same letters are at least distance 3 from each other.
# Example 2:
# s = "aaabc", k = 3
#
# Answer: ""
#
# It is not possible to rearrange the string.
# Example 3:
# s = "aaadbbcc", k = 2
#
# Answer: "abacabcd"
#
# Another possible answer is: "abcabcda"
#
# The same letters are at least distance 2 from each other.




# WRONG my first attempt was to apply each letter round-robin in order of decreasing frequency
# my second attempt was to only round-robin on a k-sized queue, where chars are added to the queue
# in order of highest frequency

# my approach should have been to use a priority queue, because while I was close to the solution,
# I should have been rearranging according to the number of chars which remain to be placed in the
# string, not just the initial counts

# I NEED TO TEST THESE IDEAS ON THE WHITEBOARD RIGOROUSLY BEFORE GOING TO CODE OR I WONT GET A JOB

# A SOLUTION
#
# class Solution(object):
#     def rearrangeString(self, str, k):
#         heap = [(-f, c) for c,f in collections.Counter(str).items()]
#         heapq.heapify(heap)
#         res = []
#         while len(res) < len(str):
#             cur = []
#             n = len(str) - len(res)
#             for _ in range(min(max(1,k), n)):
#                 if not heap:
#                     return ""
#                 f, c = heapq.heappop(heap)
#                 res.append(c)
#                 if f < -1:
#                     cur.append((f+1, c))
#             while cur:
#                 heapq.heappush(heap, cur.pop())
#         return "".join(res)

from collections import deque

def get_counts(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    return counts

class charcount:
    def __init__(self, ch, count):
        self.char = ch
        self.count = count
        self.next_use = -1
    def __repr__(self):
        return "({}, {}, {})".format(self.char, self.count, self.next_use)

class Solution:
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        if k == 0 return s

        ready = deque(sorted([charcount(ch, count) for ch, count in get_counts(s).items()], key=lambda x : x.count))
        now = deque()
        ret = []

        for i in range(len(s)):

            print("i {} Ready {} Now {}".format(i,ready,now))

            while len(now) < k and len(ready) > 0:
                now.appendleft(ready.pop())



            if len(now) == 0 or now[-1].next_use > i:
                return ""
            else:
                ccount = now.pop()

                ccount.count -= 1
                ccount.next_use = i+k

                ret.append(ccount.char)

                if ccount.count > 0:
                    now.appendleft(ccount)

        return ''.join(ret)
