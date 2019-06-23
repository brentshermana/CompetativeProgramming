# Consider a maze mapped to a matrix with an upper left corner at coordinates
# (row, column) = (0, 0). Any movement must be in increasing row or column direction.
# You must determine the number of distinct paths through the maze. You will always
# start at position (0, 0), the top left, and end up at (max(row), max(column)), the
# bottom right.

# each cell in the matrix is either open (1) or closed (0)

# return the number of paths through the matrix, modulo (10^9 + 7).
# returning the answer modulo whatever isn't really interesting though...


# There is a table cell for each matrix element.
# table[i][j] = sum(table[i-1][j], table[i][i-1])
# closed cells are always 0

def numberOfPaths(a):
    if len(a) == 0 or len(a[0]) == 1:
        return 0

    table = []
    for r in a:
        table.append([0] * len(r))

    if a[0][0] == 1:
        table[0][0] = 1

    for i in range(len(a)):
        for j in range(len(a[0])):
            # check if blocked
            if a[i][j] == 0:
                continue

            if j-1 >= 0:
                table[i][j] += table[i][j-1]
            if i-1 >= 0:
                table[i][j] += table[i-1][j]

    return table[len(a)-1][len(a[0])-1] % (10**9 + 7)

print(numberOfPaths([[1,1],[1,1]]))
