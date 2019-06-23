# given an array of integers, partition it into k subsets,
# each of which sums to the same value. Don't actually perform the
# partitioning (although that's a good followup), just return whether
# it's possible

# We CAN'T greedily consume subsets and assume that everything will work out OK
# for future subsets. Counterexample:  [10 10 10 7 7 7 7 7 7 6 6 6], K=3
# For that case, we're trying to partition into three subsets of thirty,
# which isn't possible if we form one subset using the three tens

# Recursion + backtracking approach:
#
# Filling a single subset is bounded by O(2^N), because at each point in
# the array we must try moving forward with the current element and without it,
# and we fill K such subsets. It's tempting to think that this means the time
# complexity is O(2^N * k), but it's worse than that, because there exist
# subset selections which cause further subset construction attempts to fail.
# We have one such example above. So really, for a given element in the worst
# case we would try to put it in the first set, then the second set, then the
# third set, etc. and continue failing until it successfully lands in the last set.
# That's K possible branches rather than 2, so the solution is at least O(K^N)
#
# Take a look at Leetcode's python solution... They've identified some non-obvious
# optimizations and have very clean code in their solution:
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solution/
def entry(arr, k):
    """The api entry point"""
    # There are some cases for which we can know without trying that
    # the problem can't be solved:

    # 1) The sum doesn't evenly divide
    subset_sum = sum(arr) // k
    if sum(arr) % subset_sum != 0:
        return False
    # 2) invalid input
    if k <= 0:
        return False
    # 3) not enough elements to produce the number of subsets
    if k > len(arr):
        return False
        
    taken = [False for _ in range(len(arr))]
    return rec(arr, k, taken, 0, 0, subset_sum, 0)

def rec(arr, k, taken, i, cur_sum, target_sum, filled_subsets):
    # if we've filled k of the subsets, it's trivial to fill the last one
    if filled_subsets == k-1:
        return True
    # current subset is full
    if cur_sum == target_sum:
        return rec(arr, k, taken, 0, 0, target_sum, filled_subsets+1)
    # current subset is too full
    if cur_sum > target_sum:
        return False
    # can't fill subset by going this route
    if i == len(arr):
        return False

    if not taken[i]:
        taken[i] = True
        if rec(arr, k, taken, i+1, cur_sum+arr[i], target_sum, filled_subsets):
            return True
        # if we fail, restore the previous state
        taken[i] = False
    return rec(arr, k, taken, i+1, cur_sum, target_sum, filled_subsets)

