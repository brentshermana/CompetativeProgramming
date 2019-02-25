# A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
#
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.
#
# If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.
#
# Note:
#
# The number of stones is ≥ 2 and is < 1,100.
# Each stone's position will be a non-negative integer < 231.
# The first stone's position is always 0.
# Example 1:
#
# [0,1,3,5,6,8,12,17]
#
# There are a total of 8 stones.
# The first stone at the 0th unit, second stone at the 1st unit,
# third stone at the 3rd unit, and so on...
# The last stone at the 17th unit.
#
# Return true. The frog can jump to the last stone by jumping
# 1 unit to the 2nd stone, then 2 units to the 3rd stone, then
# 2 units to the 4th stone, then 3 units to the 6th stone,
# 4 units to the 7th stone, and 5 units to the 8th stone.
# Example 2:
#
# [0,1,2,3,4,8,9,11]
#
# Return false. There is no way to jump to the last stone as
# the gap between the 5th and 6th stone is too large.


# SOLVED using DFS while tracking visited states.
# insight into what a state is is one of the key observations here.
#
# there are S stones which in the worst case could form a fully-connected
# graph, and a state is essentially an edge. So, there are as many as
# S^2 states. In the worst case we would have to traverse all of them, so
# our time and space complexity is S^2

class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        last_stone = stones[-1]
        stones = set(stones)
        states_visited = set()
        frontier = list()

        cur_state = (0, 1)  # current position, next jump length
        frontier.append(cur_state)
        states_visited.add(cur_state)

        while len(frontier) > 0:
            pos, jump_len = frontier.pop()
            if pos == last_stone:
                return True

            next_pos = pos + jump_len
            if next_pos in stones:
                for next_jump_len in [jump_len + 1, jump_len, jump_len - 1]:
                    next_state = (next_pos, next_jump_len)
                    if next_state not in states_visited:
                        states_visited.add(next_state);
                        frontier.append(next_state)
        return False