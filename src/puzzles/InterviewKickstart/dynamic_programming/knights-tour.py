# you are given a phone number dial as follows:

# 1 2 3
# 4 5 6
# 7 8 9
# - 0 -

# and a knight (like in chess) starting at a particular digit.
# count the number of unique phone numbers of a given length that
# can be produced by the knight

# table formulation!
# table[1][start_coord] = 1
# table[1][<other_coords>] = 0
# table[i][c1] = Sum over all c2's adj to c1 -> table[i-1][c2]
# solution is sum(table[number_length]) 

import itertools as it
from collections import defaultdict

def numPhoneNumbers(start_digit, number_length):
    if number_length == 0:
        return 0

    board = [[1 ,2, 3],
             [4 ,5, 6],
             [7 ,8, 9],
             [-1,0,-1]]

    valid_coords = set(
        ( (r,c) for r, c in it.product(range(len(board)), range(len(board[0]))) if board[r][c] != -1)
    )

    valid_moves = defaultdict(list)
    for i, j in valid_coords:
        little = [1, -1]
        big = [2, -2]
        for di, dj in it.chain(it.product(little, big), it.product(big, little)):
            coord = (di+i, dj+j)
            if coord in valid_coords:
                valid_moves[(i, j)].append(coord)

    table =    [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

    # find the start digit and mark it as '1' in the table
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == start_digit:
                table[i][j] = 1

    # perform a -1 adjustment to the range because the length is already 1 when we start
    # at the start digit
    for _ in range(number_length-1):
        new_table = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        for i, j in valid_coords:
            for ii, jj in valid_moves[(i, j)]:
                new_table[i][j] += table[ii][jj]
        table = new_table
    return sum((sum(row) for row in table))

print(numPhoneNumbers(1,3))

