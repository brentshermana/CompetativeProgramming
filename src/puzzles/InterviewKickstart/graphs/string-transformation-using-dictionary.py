# given an array of strings, return an array of strings
# representing the transformation from a start word
# to a stop word by changing only one character at a time
# and ensuring all intermediate words are in dictionary

# make sure the path is as short as possible

# assume all strings are equal length. The dictionary may
# contain duplicates.


# Complete the function below.

from collections import defaultdict
from collections import deque

def string_transformation(words, start, stop):

    visited = set() # set of strings
    
    # for simplicity, let's make sure 'stop'
    # and 'start' are in the dictionary
    words.append(stop)
    
    # create a map of the following format:
    # [dog, bog] -> {_og: [dog, bog]}
    adj_map = defaultdict(set)

    def blankify(s, i):
        return s[:i] + '_' + s[i+1:]
    for word in words:
        for i in range(len(word)):
            adj_map[blankify(word, i)].add(word)
    def adj(s):
        for i in range(len(s)):
            yield from (a for a in adj_map[blankify(s, i)] if a != s)
        
    bp = {start: None}    
    
    visited.add(start)
    q = deque()
    q.appendleft(start)
    while len(q) > 0:
        s = q.pop()
        if s == stop:
            # form the path using backpointers
            path = []
            while s is not None:
                path.append(s)
                s = bp[s]
            path.reverse()
            return path
        for a in adj(s):
            if a not in visited:
                bp[a] = s
                visited.add(a)
                q.appendleft(a)
    # no path
    return ["-1"]

print(string_transformation(["cat", "hat", "bad", "had"], "bat", "had"))