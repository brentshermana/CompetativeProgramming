# At Quora, we have aggregate graphs that track the number of upvotes we get each day.
#
# As we looked at patterns across windows of certain sizes, we thought about ways
# to track trends such as non-decreasing and non-increasing subranges as efficiently
# as possible.
#
# For this problem, you are given N days of upvote count data, and a fixed window size K.
# For each window of K days, from left to right, find the number of non-decreasing subranges
# within the window minus the number of non-increasing subranges within the window.
#
# A window of days is defined as contiguous range of days. Thus, there are exactly N−K+1
# windows where this metric needs to be computed. A non-decreasing subrange is defined as
# a contiguous range of indices [a,b], a<b, where each element is at least as large as the
# previous element. A non-increasing subrange is similarly defined, except each element is
# at least as large as the next. There are up to K(K−1)/2 of these respective subranges
# within a window, so the metric is bounded by [−K(K−1)/2,K(K−1)/2].
#
# Constraints
# 1≤N≤100,000 days
# 1≤K≤N days
#
# Input Format
# Line 1: Two integers, N and K
#
# Line 2: N positive integers of upvote counts, each integer less than or equal to 109.
#
# Output Format
# Line 1..: N−K+1 integers, one integer for each window's result on each line
#
# Sample Input
# 5 3
# 1 2 3 1 1
#
#
# Sample Output
# 3
# 0
# -2
#
#
# Explanation
# For the first window of [1, 2, 3], there are 3 non-decreasing subranges and 0
# non-increasing, so the answer is 3. For the second window of [2, 3, 1], there is
# 1 non-decreasing subrange and 1 non-increasing, so the answer is 0. For the third
# window of [3, 1, 1], there is 1 non-decreasing subrange and 3 non-increasing,
# so the answer is -2.

# my solution, evidently, doesn't work. It gets timeouts and wrong answers.....

import sys
import heapq

lines = sys.stdin.readlines()
N,K = tuple([int(x) for x in lines[0].split()])
seq = [int(x) for x in lines[1].split()]

def get_ranges(f): # f is just max() or min()
    #print()
    #print("Call for function {}".format(f))
    ranges = []
    for i in range(0, N-K+1):
        #print("Considering base index {}".format(i))
        for k in range(2, K+1): # intervals of len 1 are trivial and don't really matter
            if f(seq[i+k-1], seq[i+k-2]) == seq[i+k-1]:
                #print("k == {} works".format(k))
                # increment appropriate values
                ranges.append( (i+k,i) ) # add in reverse
                #print(count)
            else:
                break # subseq of higher k that meets the requirement won't exist
    return ranges

noninc_ranges = get_ranges(min)
heapq.heapify(noninc_ranges) # sorted by increasing right bound
nondec_ranges = get_ranges(max)
heapq.heapify(nondec_ranges)

current_noninc = [] # sorted by increasing left bound
current_nondec = []

for i in range(N-K+1):
    #print()
    #print("I: {}".format(i))

    # remove obsolete ranges
    while len(current_noninc) > 0 and current_noninc[0][0] < i:
        #print("Remove decreasing range {}".format())
        heapq.heappop(current_noninc)

    while len(current_nondec) > 0 and current_nondec[0][0] < i:
        #print("Remove increasing range {}".format())
        heapq.heappop(current_nondec)


    # add new ranges
    while len(noninc_ranges) > 0 and noninc_ranges[0][0] <= i+K:

        r, l = heapq.heappop(noninc_ranges)
        heapq.heappush(current_noninc, (l,r,))
        #print("Add decreasing range {}".format((l, r,)))
    while len(nondec_ranges) > 0 and nondec_ranges[0][0] <= i+K:

        r, l = heapq.heappop(nondec_ranges)
        heapq.heappush(current_nondec, (l,r,))
        #print("Add increasing range {}".format((l, r,)))

    print(len(current_nondec) - len(current_noninc))


