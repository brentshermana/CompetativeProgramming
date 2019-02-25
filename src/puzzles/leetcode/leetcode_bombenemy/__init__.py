# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.
#
# Example:
# For the given grid
#
# 0 E 0 0
# E 0 W E
# 0 E 0 0
#
# return 3. (Placing a bomb at (1,1) kills 3 enemies)

# solved in O(rc) time:
# pass 1: map coord to number of enemies killed in the given col
# pass 2: map coord to number of enemies killed in the given row
# pass 3: get the max


class Solution:
    def maxKilledEnemies(self, g):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        kill = {}

        rows = len(g)
        if rows == 0: return 0
        cols = len(g[0])
        if cols == 0: return 0

        def flush(d, l, c):
            while len(l) > 0:
                k = l.pop()
                d[k] = d.get(k, 0) + c

        for r in range(rows):
            ec = 0
            l = []
            for c in range(cols):
                if g[r][c] == 'W':
                    flush(kill, l, ec)
                    ec = 0
                if g[r][c] == 'E':
                    ec += 1
                if g[r][c] == '0':
                    l.append((r, c,))
            flush(kill, l, ec)

        # almost the same as the previous block
        for c in range(cols):
            ec = 0
            l = []
            for r in range(rows):
                if g[r][c] == 'W':
                    flush(kill, l, ec)
                    ec = 0
                if g[r][c] == 'E':
                    ec += 1
                if g[r][c] == '0':
                    l.append((r, c,))
            flush(kill, l, ec)

        if len(kill) == 0:
            return 0
        else:
            return max(kill.values())