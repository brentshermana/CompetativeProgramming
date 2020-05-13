# The interesting part of this challenge was the optimization that
# went into the trie pruning (removing words after matching)
# and using a very SIMPLE trie structure instead of a complete
# class with methods

# SLOW approach (didn't use)
# for each position in the board ( O(board_size) )
#   for each word starting with the letter there ( O(words) )
#     run dfs to attempt to match the full string recursively ( O(4^word_len) )
#
# the recursive function accepts a list of positions that have already been used (can't revisit),
# the remaining letters to match and the current position
#

# MY approach
# 1) build up a trie
# for each position on the board: ( O(board_size) )
#   dfs in all directions, looking for all words ( O() )

# VERY simple trie
class Node:
    def __init__(self):
        self.end_i = -1
        self.d = {}

def get_matches(board, i, j, n):
    if n.end_i >= 0:
        # optimization: remove a node's "word end" marker after it's been matches
        x = n.end_i
        n.end_i = -1
        yield x
    if len(board) > i >= 0 and len(board[0]) > j >= 0:
        if board[i][j] in n.d:
            # overwriting the state of the board is my way of tracking which
            # characters have been used (a character can only be used once in a match)
            temp, board[i][j] = board[i][j], ''

            cur_node = n.d[temp]
            for ii, jj in ((0, 1),(1, 0),(-1, 0),(0, -1)):
                yield from get_matches(board, i+ii, j+jj, cur_node)

            board[i][j] = temp

            # optimization: remove leaf nodes that are no longer word endings
            #               to reduce future matching work
            if cur_node.end_i < 0 and len(cur_node.d) == 0:
                n.d.pop(board[i][j])


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build a trie
        trie = Node()
        for i, w in enumerate(words):
            n = trie
            for c in w:
                if c not in n.d:
                    n.d[c] = Node()
                n = n.d[c]
            n.end_i = i

        sol = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                for match in get_matches(board, i, j, trie):
                    sol.add(match)
        return [words[i] for i in sol]
