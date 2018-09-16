# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
#
# The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
#
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.
#
# Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.
#
# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
#   1
#  / \
# v   v
# 2-->3
# Example 2:
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.



# I couldn't figure out the solution, but this was posted on leetcode by /u/JadenPan
#
# We can not simply apply the code from REDUNDANT CONNECTION I, and add codes checking duplicated-parent only.
# Here are 2 sample failed test cases:
# [[4,2],[1,5],[5,2],[5,3],[2,4]]
# got [5,2] but [4,2] expected
# and
# [[2,1],[3,1],[4,2],[1,4]]
# got [3,1] but [2,1] expected
# (Thanks @niwota and @wzypangpang )
# The problem is we can not consider the two conditions separately, I mean the duplicated-parents and cycle.
# This problem should be discussed and solved by checking 3 different situations:
#
# No-Cycle, but 2 parents pointed to one same child
# No dup parents but with Cycle
# Possessing Cycle and dup-parents
# Those 2 failed test cases are all in situation 3), where we can not return immediately current edge when we found something against the tree's requirements.
# The correct solution is detecting and recording the whole cycle, then check edges in that cycle by reverse order to find the one with the same child as the duplicated one we found.
# A more clear explanation and code have been posted by @niwota
# https://discuss.leetcode.com/topic/105087/share-my-solution-c