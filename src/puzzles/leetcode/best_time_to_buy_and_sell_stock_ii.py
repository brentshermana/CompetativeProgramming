# this was marked easy on LeetCode, but took me awhile to figure out the
# edge cases, and how to iterate through the array correctly. should revisit!



# here's the cleverest solution (not mine):
def maxProfit(a):
    length=len(prices)
    if length<2:return 0
    dp=0
    for i in range(1,length):
        if prices[i]>prices[i-1]:dp=dp+prices[i]-prices[i-1]
    return dp



# you may NOT hold and also buy more, you're either holding or not holding

# the list of prices is a series of peaks and valleys
# * buy at any local maxima
# * sell at any local minima

# how do we define a local maxima or minima? it's not obvious
# a position is a local maxima if in either direction, it goes down before going up!
# * in some cases you need to scan more than one space, for example with duplicates!
# * 4 5 6 <-- obviously 5 is not a local max
# * 4 5 5 5 5 5 5 5 6 <-- is the first 5 a local max? no, but we need a linear scan to check
# * to avoid the linear scan, we may be able to use DP? a cell is a local max if the adjacent cells
#   are not, AND the current cell is >= to them. that handles the case where we have a list of maxes
#

class Solution:
    def maxProfit(self, a: List[int]) -> int:
        # duplicate numbers are the edge case we're solving for here! Otherwise computing local
        # max, min is easy
        i = 0
        holding = None
        profit = 0
        while i < len(a):
            # compute next_i, the index of the next element that does not equal the current one
            # we ensure prev_i is always i-1 by only considering the first element in each
            # sequence of a repeated number
            next_i = i+1
            while next_i < len(a) and a[i] == a[next_i]:
                next_i += 1

            if holding is None:
                # not holding stock: look for local min
                if ( i == 0 or a[i] < a[i-1] ) and ( next_i == len(a) or a[i] < a[next_i] ):
                    holding = a[i]
            else:
                # holding stock: look for local max
                if ( i == 0 or a[i] > a[i-1] ) and ( next_i == len(a) or a[i] > a[next_i] ):
                    profit += a[i] - holding
                    holding = None
            i = next_i
        return profit
