# consider a row of n coins of values v1, ..., vn.
# In a turn, a player selects either the first or last roin, removes it
# from the row, and gets points equal to the value of the coin
# Determine the maximum possible amound of money you can get
# if you move first, ASSUMING the other player also plays optimally

# the table has two dimensions: the start of the coin range, and the end

# if there is one coin, take it. The value is the value of the coin
# if there are two coins, take the higher one. The value is the value of the higher coin
#   - put more generally: the value is the value of the greater of the two possible
#     resultant 'states'

# My first thought was, when filling in each cell, to say:
# if I take x in {leftmost, rightmost}:
#     my opponent will assume the value at i-1, which will bp to the previous j value
#         table[i][j] = v[j] + table[i-2][bp[ <whatever the j is for the result of the opponent's move> ]]

def maxWin(v):

    # although the "full" table is V^2, we really only need three rows at any one time:
    # 1) The row we are building, where each range is of length i
    # 2) The row representing the opponent's turn, where each range is of length i-1
    # 3) The row representing our next turn, where each range is of length i-2

    # initial values server as "bounds protection"
    # for these initial values, we need the +1 and +2 because every level you go
    # "down", the row length increases by 1
    table = {-1: [0 for _ in range(len(v)+2)],
              0: [0 for _ in range(len(v)+1)]}
    # point to the state in the previous layer resulting
    # from producing a move
    # we initialize to 0 for "i=0" because it doesn't matter, the values from
    # all previous states are the same
    bp = {0: [0 for _ in range(len(v)+1)]}

    for i in range(1, len(v)+1):
        # i indicates the length of the coin array
        table[i] = [-1 for _ in range(len(v)+1-i)]
        bp[i] =    [-1 for _ in range(len(v)+1-i)]
        for j in range(0, len(v)+1-i):
            # j indicates the index which is the start of the range, inclusive
            
            # outcome = coin_value + my score from the rest of the game
            # ... coin value
            best_outcome_right = v[j+i-1]
            # ... opponent moves
            jj = bp[i-1][j]
            # ... best score I could get from after opponent's move
            best_outcome_right += table[i-2][jj]

            best_outcome_left = v[j]
            jj = bp[i-1][j+1]
            best_outcome_left += table[i-2][jj]

            # set the table values
            if best_outcome_left > best_outcome_right:
                table[i][j] = best_outcome_left
                bp[i][j] = j+1
            else:
                table[i][j] = best_outcome_right
                bp[i][j] = j

        # get rid of table values we no longer need
        # (results in linear space, rather than quadratic)
        # del bp[i-1]
        # del table[i-2]
        
    return max(table[len(v)])

print(maxWin([8, 15, 3, 7]))
