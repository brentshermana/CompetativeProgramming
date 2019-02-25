# Freedom Trail
# Difficulty:Hard
#
# In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.
#
# Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.
#
# Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button.
# At the stage of rotating the ring to spell the key character key[i]:
# You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
# If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.
# Example:
#
# * a picture of the chars 'godding' wrapped in a ring
#
#
# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
#  For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
#  For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
#  Also, we need 1 more step for spelling.
#  So the final output is 4.
# Note:
# Length of both ring and key will be in range 1 to 100.
# There are only lowercase letters in both strings and might be some duplcate characters in both strings.
# It's guaranteed that string key could always be spelled by rotating the string ring.


# I GOT IT! it seems like optimizations I used (heapq) allowed me to get better runtimes compared to others
# , but their solutions are more general and therefore worth looking at.
#
# Below: A dynamic programming approach using hashing
#
# def findRotateSteps(self, ring, key):

#         # the distance between two points (i, j) on the ring
#         def dist(i, j):
#             return min(abs(i - j), len(ring) - abs(i - j))
#         # build the position list for each character in ring
#         pos = {}
#         for i, c in enumerate(ring):
#             if c in pos:
#                 pos[c].append(i)
#             else:
#                 pos[c] = [i]
#         # the current possible state: {position of the ring: the cost}
#         state = {0: 0}
#         for c in key:
#             next_state = {}
#             for j in pos[c]:  # every possible target position
#                 next_state[j] = float('inf')
#                 for i in state:  # every possible start position
#                     next_state[j] = min(next_state[j], dist(i, j) + state[i])
#             state = next_state
#         return min(state.values()) + len(key)


def rot_cost(i, j, n):
    return min(abs(i - j), min(i, j) + n - max(i, j))


def ch_indices(s):
    ret = {}
    for i, c in enumerate(s):
        l = ret.get(c, [])
        l.append(i)
        ret[c] = l
    return ret


import heapq as hq


class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        visited = set()
        ch_i = ch_indices(ring)

        q = [(0, 0, 0)]  # queue elements are cost_so_far, key_index, ring_index
        while True:
            total_cost, key_i, ring_i = hq.heappop(q)

            if key_i == len(key):
                return total_cost

            state = (key_i, ring_i,)

            if state in visited:
                continue
            else:
                visited.add(state)

                for next_ring_i in ch_i[key[key_i]]:
                    hq.heappush(
                        q,
                        (total_cost + rot_cost(ring_i, next_ring_i, len(ring)) + 1,
                         key_i + 1,
                         next_ring_i,)
                    )