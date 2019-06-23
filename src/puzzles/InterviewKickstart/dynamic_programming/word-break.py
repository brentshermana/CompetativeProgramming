# You are given a dictionary containing distinct words, and another string x
# segment the txt string such that all the segments occur in the original string
# and all these segments exist in the dictionary

# put another way: plit the string using spaces so that each segment is in the
# dictionary

# return an ARRAY of ALL possible segmentations

# *** a single word from the dictionary can be used multiple times

# analysis: Each string in d will have at least len(1). So we can
# have at most len(x) splitting points.
# So, we can formulate a "state" as a len(x) dimensional boolean array
# ... but I don't like that, because there are 2^len(x) of those
# perhaps we can have the state just be the position we have reached so far?

# THE TABLE:
# - initialize all cells to [] (unreachable)
# - each cell contains a list of all possible predecessors,
# because we have to get all possible segmentations

# Is it better to construct the strings incrementally, or at the end based on
# only the things we know are solutions? I think it depends on the given problem...
# let's assume the number of correct solutions << the number of possible strings

# perform FASTER string matching by putting 'd' into a trie
# ... but that won't save us from the worst case len(x)^2 runtime

# from collections import defaultdict

# class TrieNode:
#     def __init__(self):
#         self.succ = defaultdict(TrieNode)
#         self.is_end = False

#     def add(self, w, i):
#         if i == len(w):
#             self.is_end = True
#         else:
#             self.succ[w[i]].add(w, i+1)

#     def matches(self, s, i):
#         """
#         return a list of the indices of s that match against
#         elements of this 
#         """


def solver(d, x): # dictionary and string

    # we don't have any use for empty strings
    d = [s for s in d if len(s) > 0]

    # each element of the table is an array pointing to locations
    # further ahead in the array that we can go to
    table = [[] for _ in range(len(x))]
    
    # table construction phase: go from high indices to low ones
    for i in range(len(x), -1, -1):
        if i != len(x) and len(table[i]) == 0:
            # 'unreachable' position
            continue
        for w in d:
            if len(w) > i:
                # too long
                continue
            elif x[i-len(w):i] == w:
                # assign the predecessor
                table[i-len(w)].append(i)

    # result construction phase
    # although it's less efficient, it's easier to do recursively
    ret = []
    def fillret(i, segments):
        if i == len(x):
            ret.append(' '.join(segments))
        else:
            for j in table[i]:
                segments.append(x[i:j])
                fillret(j, segments)
                segments.pop()
    fillret(0, [])

    return ret
