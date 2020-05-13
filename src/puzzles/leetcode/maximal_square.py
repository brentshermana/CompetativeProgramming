
# HERE'S MY BEST SOLUTION. it's textbook DP.

class Solution:
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0

        max_len = 0
        prev_row = None
        row = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '0':
                    row.append(0)
                else:
                    # boundary checks: we need to build up our solution
                    # using the square below, the square to the left,
                    # and the square down and to the left
                    if r == 0 or c == 0:
                        # if any of them are missing, we can't build up from them
                        # start with a square of 1
                        val = 1
                    else:
                        # all three values exist. each val represents the side len of the largest
                        # square building up to that (top right) corner so far,
                        # so we take the smallest of those vals and
                        val = 1 + min(row[c-1], prev_row[c-1], prev_row[c])
                    row.append( val )
                    max_len = max(max_len, val)
            prev_row = row
            row = []
        # return the area, not the side len
        return max_len * max_len



# naive approach: build up to a square in some direction (eg up and to the left)
#                 from each coordinate in the matrix
# improvement: specialized "square" bfs, remember places you have been IN A REALLY CLEVER WAY

# when we start by looking at one point, we already have a square. What can we do to maintain the square?
# expand one space in each dimension every time! only mark squares as 'visited' after we correctly expand into them
# * NOTE: it is possible for a small square to intersect with a big square, which can result in some of the big square's
#         ones as used! BUT not all of them will be marked as used, so let's say you can attempt to explore a cube as
#         long as your starting point is not marked used! you're allowed to expand into used territory


# HERE IS MY FIRST SOLUTION. it technically works, but there are better ones by far (below!)

import itertools

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # edge cases for empty matrix:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        best_cube_area = 0
        explored = set()
        for start_i, start_j in itertools.product(range(len(matrix)), range(len(matrix[0]))):
            if (start_i, start_j) in explored:
                continue
            if matrix[start_i][start_j] == '0':
                continue
            print((start_i, start_j))

            # just need to track the bounds
            max_i = start_i
            min_i = start_i
            max_j = start_j
            min_j = start_j

            # greedily pursued each corner expansion direction
            for di, dj in itertools.product([-1, 1], [-1, 1]):
                expand = True
                while expand:
                    if di == -1:
                        new_i = min_i - 1
                        if new_i < 0:
                            break
                    else:
                        new_i = max_i + 1
                        if new_i >= len(matrix):
                            break
                    if dj == -1:
                        new_j = min_j - 1
                        if new_j < 0:
                            break
                    else:
                        new_j = max_j + 1
                        if new_j >= len(matrix[0]):
                            break

                    # check that each of the newly added squares is '1'
                    for i in range(min_i, max_i+1):
                        if matrix[i][new_j] == '0':
                            expand = False
                            break
                    for j in range(min_j, max_j+1):
                        if matrix[new_i][j] == '0':
                            expand = False
                            break
                    if matrix[new_i][new_j] == '0':
                        expand = False

                    if expand:
                        max_i = max(max_i, new_i)
                        min_i = min(min_i, new_i)
                        max_j = max(max_j, new_j)
                        min_j = min(min_j, new_j)

            # record final cube area
            best_cube_area = max(best_cube_area, (max_i + 1 - min_i) * (max_j + 1 - min_j) )

            # mark cube squares as recorded
            for i in range(min_i, max_i+1):
                for j in range(min_j, max_j+1):
                    explored.add( (i, j) )


        return best_cube_area
