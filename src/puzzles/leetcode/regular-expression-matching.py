# SUCCESS eventually, this one took me a little while

# given an input string s and a pattern p, implement regular expression
# matching with support for . and *
# NOTE that * means "zero or more of the preceding character", not
# "match anything"

# We're trying to match the entire string, so just return a boolean

# is there any sort of DP we can perform here? YES
# 2D array which takes si and pi and says whether we've visited that path before.
# it does not need to say whether we were successful

from collections import defaultdict

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # tokenize p into a list of strings by merging
        # stars with the preceding character:
        p_new = []
        for c in p:
            if c == '*':
                p_new.append(p_new.pop()+c)
            else:
                p_new.append(c)
        p = p_new

        # primary data structures
        checked = defaultdict(lambda: defaultdict(bool))
        todo = []

        # utility for memo and bounds checking
        def add(si, pi):
            if si > len(s) or pi > len(p):
                return
            if not checked[si][pi]:
                checked[si][pi] = True
                todo.append((si, pi))

        def is_match(a, b):
            if a[0] == '.':
                return True
            else:
                return a[0] == b[0]

        add(0, 0)
        while len(todo) > 0:
            si, pi = todo.pop()

            if si == len(s) or pi == len(p):
                # return immediately upon success
                if si == len(s) and pi == len(p):
                    return True
                # edge case: if the current pattern is a star,
                # we can skip it:
                if pi < len(p) and p[pi][-1] == '*':
                    add(si, pi+1)
            else:
                if p[pi][-1] == '*':
                    # don't utilize star
                    add(si, pi+1)
                    # utilize star
                    if is_match(p[pi], s[si]):
                        add(si+1, pi)
                elif p[pi] == '.':
                    # . matches anything
                    add(si+1, pi+1)
                else:
                    # normal character matching
                    if s[si] == p[pi]:
                        add(si+1, pi+1)

        # nothing worked
        return False

# here was my original recursive solution, for reference.
# it wasn't totally correct.

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         # trivial recursive solution
#         def rec(si, pi):
#             if si == len(s) or pi == len(p):
#                 # a star can match against zero characters
#                 if pi == len(p) or p[pi] != '*':
#                     return si == len(s) and pi == len(p)

#             if p[pi] == '.':
#                 return rec(si+1, pi+1)
#             if p[pi] == '*':
#                 # either we're done with the star, or we're using it
#                 return rec(si+1, pi) or rec(si, pi+1)
#             # any other char
#             return s[si] == p[pi] and rec(si+1, pi+1)
#         return rec(0, 0)
