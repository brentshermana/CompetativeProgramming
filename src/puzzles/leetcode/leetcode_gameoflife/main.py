# Game of Life
# Difficulty:Medium
#
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
#
# Example:
#
# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
# Follow up:
#
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

# SOLVED. non-in place is trivial, I implemented with linear O(n) time, the space of a single row. I don't think it's
# possible to solve with constant memory overhead

# I TAKE THAT BACK you can solve with no memory overhead by storing the next state of each cell in that cell's value, just
# in an unused bit: https://leetcode.com/problems/game-of-life/discuss/73370/Python-solution-O(MN)-time-O(1)-space

class Solution:
    def gameOfLife(self, b):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(b)
        n = len(b[0])

        def valid_coord(r, c, m, n):
            return r >= 0 and c >= 0 and r < m and c < n

        def live_neighbors(b, m, n, row):
            live = [0 for _ in range(n)]
            for r in range(row - 1, row + 2):
                for c in range(n):
                    if valid_coord(r, c, m, n) and b[r][c] == 1:
                        # tally
                        if valid_coord(r, c + 1, m, n):
                            live[c + 1] += 1
                        if valid_coord(r, c - 1, m, n):
                            live[c - 1] += 1
                        if not r == row:
                            live[c] += 1
            return live

        def compute_update(b, m, n, row):
            live = live_neighbors(b, m, n, row)
            update = [0 for _ in range(n)]
            for c in range(n):
                if b[row][c] == 1:
                    if live[c] < 2:
                        update[c] = 0
                    elif live[c] < 4:
                        update[c] = 1
                    else:
                        update[c] = 0
                elif live[c] == 3:
                    update[c] = 1
            return update

        prev_update = compute_update(b, m, n, 0)
        for r in range(1, m):
            cur_update = compute_update(b, m, n, r)
            b[r - 1] = prev_update
            prev_update = cur_update
        b[m - 1] = prev_update  # necessary for final row