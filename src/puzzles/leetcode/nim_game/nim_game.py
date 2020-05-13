#You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

#Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

#Example:

#Input: 4
#Output: false
#Explanation: If there are 4 stones in the heap, then you will never win the game;
#             No matter 1, 2, or 3 stones you remove, the last stone will always be
#             removed by your friend.


# OPTIMAL SOLUTION: plotting out the actual structure ends up looking like this:
#
# 0123456789
# TTTFTTTFTTTF...
#
# so the solution is just a constant time check:
K = 3
from collections import deque
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n == 0:
            return False
        return n % (K+1) != 0

# FIRST ATTEMPT: sort-of DP/Memoization in linear time
K = 3
from collections import deque
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= K:
            return True

        # use a deque for optimal memory
        dp = deque()
        for _ in range(K):
            dp.append(True)

        # the current setup shows solutions for 1...K,
        # so we need to iterate n-K more times to have the final solution
        for i in range(n-K):
            # winning move exists if we can move the state to a losing state
            # for opponent's turn
            winning_move_exists = False in dp
            dp.append(winning_move_exists)
            dp.popleft()

        return dp.pop()
