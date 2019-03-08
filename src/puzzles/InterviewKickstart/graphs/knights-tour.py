# given a rows * cols chessboard, and a start and end coordinate,
# calculate the minimum number of moves needed to reach the end coordinate
# using a knight in chess

# return -1 if the path can't be found

from collections import deque, defaultdict
from itertools import product

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    # Write your code here.

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def adj(r, c):
        # could have been more clever here, but
        # would impact readability
        for dx, dy in product((1, -1), (2, -2)):
            r_new, c_new = r+dx, c+dy
            if in_bounds(r_new, c_new):
                yield r_new, c_new
        for dx, dy in product((2, -2), (1, -1)):
            r_new, c_new = r+dx, c+dy
            if in_bounds(r_new, c_new):
                yield r_new, c_new

    visited = defaultdict(lambda: defaultdict(bool))

    q = deque()
    q.appendleft((start_row, start_col, 0))
    visited[start_row][start_col] = True
    while len(q) > 0:
        r, c, moves = q.pop()
        if r == end_row and c == end_col:
            return moves
        for r_new, c_new in adj(r, c):
            if not visited[r_new][c_new]:
                visited[r_new][c_new] = True
                q.appendleft((r_new, c_new, moves+1))
    # no path
    return -1