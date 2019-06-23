# a person can take some number of stairs for each step. Count
# the number of ways to reach the nth step

# there is 1 way to reach the first stair
# there are two ways to reach the second stair
# there are 111 12 21 three ways to reach the third stair

# to formulate this as a table, if we are at step i, which we can reach in I ways,
# and we can move directly to j, J += I

def countWaysToClimb(steps, n):
    # step '0' is not actually a step. It's right before the first step
    table = [0 for _ in range(n+1)]
    table[0] = 1 # one way to do nothing
    for i in range(n+1):
        for inc in steps:
            if i+inc > n:
                continue
            table[i+inc] += table[i]
    return table[n]


