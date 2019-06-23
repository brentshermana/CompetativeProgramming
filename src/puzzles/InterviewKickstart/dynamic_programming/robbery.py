# There are n houses built in a line, each of which contains some value in it.
# A thief is going to steal the maximal value in these houses,
# but he cannot steal in two adjacent houses because the owner of a stolen
# house will tell his two neighbors on the left and right side.

# What is the maximal stolen value?

# approach: If we 'consume' the houses sequentially, we don't really need to keep
# track of which ones are 'blocked' due to having a neighbor robbed, or
# whether they were robbed themselves. We just know that everything to our left is
# consumed, and everything to our right is free

# example: 10, 2, 3, 9
# (obviously the answer is 19. I'm picking this example problem to confirm we're not
# making the greedy mistake of robbing 2 or 3)
# We should take 9 if [9 + subproblem(index 1)] > [subproblem(index 1)]

def maxStolenValue(houses):
    if len(houses) == 0:
        return 0

    table = [0 for _ in range(len(houses))]
    table[0] = houses[0]
    for i in range(1, len(houses)):
        options = [table[i-1], # rob previous house instead of this one
                   houses[i]]  # rob this house, leave previous one

        # if we rob this house, we still get the loot from the subproblem starting
        # one before the house we passed over
        if i-2 >= 0:
            options[1] += table[i-2]

        table[i] = max(options)

    return table[len(houses)-1]