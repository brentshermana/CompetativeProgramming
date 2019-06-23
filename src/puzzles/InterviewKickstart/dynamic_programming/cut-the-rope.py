# Given a rope with length n, find the maximum value maxProduct
# that can be achieved for product len[0] * len[1] * ... * len[m - 1],
# where len[] is the array of lengths obtained by cutting the given rope into m parts.

# Note that
# there should be atleast one cut, i.e. m >= 2.
# All m parts obtained after cut should have non-zero integer valued lengths.

# Where are the subproblems?
# let's say the length is 4.
# 1 * 3 or 3 * 1 or 2 * 2

# The subproblems are the lengths:
# subproblem[1] -> 1
# subproblem[2] -> max(2, subproblem[1]*1)
# subproblem[3] -> max(3, subproblem[1]*subproblem[2])
# subproblem[4] -> max(4, subproblems[1 and 3], subproblems[2 and 2])

# This will be an N^2 solution, not because there are N^2 cells, but
# because filling each cell takes N time rather than constant time

def max_product_from_cut_pieces(n):
    # initial value for each subproblem is just the result of taking the entire length
    # as one piece. If we decide to use a product of subproblems instead,
    # it must be greater than this value
    table = [x+1 for x in range(n)]
    # ... but the final solution must be in at least 2 pieces
    table[n-1] = 0

    # to fill cell i, which corresponds to length i+1 ...
    for i in range(1, n):
        # we need to iterate through all possible combinations
        # of 2 subproblems. This is sufficient because either of these
        # subproblems can be a product of multiple numbers in turn
        
        top = i-1
        bottom = 0 # 0 actually represent length 1 in the table
        while bottom <= top:
            table[i] = max(table[i], table[bottom]*table[top])
            top -= 1
            bottom += 1

    return table[n-1]
