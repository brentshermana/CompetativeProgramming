# Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B. The integer B denotes that from any place (suppose the index is i) in the array A, you can jump to any one of the place in the array A indexed i+1, i+2, …, i+B if this place can be jumped to. Also, if you step on the index i, you have to pay Ai coins. If Ai is -1, it means you can’t jump to the place indexed i in the array.
#
# Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed N using the minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should take to get to the place indexed N using minimum coins.
#
# If there are multiple paths with the same cost, return the lexicographically smallest such path.
#
# If it's not possible to reach the place indexed N then you need to return an empty array.
#
# Example 1:
# Input: [1,2,4,-1,2], 2
# Output: [1,3,5]
# Example 2:
# Input: [1,2,4,-1,2], 1
# Output: []
# Note:
# Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm, if and only if at the first i where Pai and Pbi differ, Pai < Pbi; when no such i exists, then n < m.
# A1 >= 0. A2, ..., AN (if exist) will in the range of [-1, 100].
# Length of A is in the range of [1, 1000].
# B is in the range of [1, 100].


import copy

class Solution:

    # if I were to improve this solution I would do so by making the backpointer collection more efficient.
    # I can do comparisons on the fly to enforce the lexicograhphic property of the final path

    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if len(A) == 0:
            return []

        c = [None] * len(A) # cost for best know way(s) to get to each index
        bp = [None] * len(A) # each element is None, or a list of backpointers
        c[0] = A[0]

        for i in range(len(A)):

            # if the leetcode_freedomtrail 'base' location is inaccessible, don't calculate successors
            if c[i] == None:
                continue

            for jmp in range(i+1, min(i+B+1, len(A))):

                # if successor is inaccessible, don't consider it
                if A[jmp] == -1:
                    continue

                current_cost = c[i] + A[jmp]

                # discard all previous backpointers to replace with new best path
                if c[jmp] is None or current_cost < c[jmp]:
                    c[jmp] = current_cost
                    bp[jmp] = [i]

                # equally good path -- just add to the list
                elif current_cost == c[jmp]:
                    bp[jmp].append(i)

        # get the paths:
        rev_paths = []
        q = [[len(A)-1]] # queue starting with incomplete path: the final index
        while len(q) > 0:
            inc_path = q.pop()
            if bp[inc_path[-1]] == None:
                # the path is finished
                rev_paths.append(inc_path)
            else:
                for pred_bp in bp[inc_path[-1]]:
                    new_inc_path = copy.copy(inc_path)
                    new_inc_path.append(pred_bp)
                    q.append(new_inc_path)

        # the solution wants index-1 based, so we increment each value as well as reverse
        paths = map(lambda rev_path : list(map(lambda x : x + 1, reversed(rev_path))), rev_paths)
        # remove incomplete paths, which start at the end and then stop before reaching the beginning
        paths = list(filter(lambda path : path[0] == 1, paths))

        if len(paths) == 0:
            return [] # no path, return empty list
        else:
            return min(paths) # does lexicographical comparisons
