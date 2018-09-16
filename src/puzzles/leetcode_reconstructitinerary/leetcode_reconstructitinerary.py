# Reconstruct Itinerary
# Difficulty:Medium
#
# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
#
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:
#
# Input: tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:
#
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

# I DIDNT GET THIS ONE.
# There was a clever solution which I wouldn't have gotten detailed here:
# https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C++
# essentially what was required was deducing that for there to be a single path which traverses the entire graph,
# only one part of the graph can be the 'dead end' part, and the rest is composed of cycles where you can't reach
# any dead end. Here's the code for that, but it's hard to understand without working out an example:

# def findItinerary(self, tickets):
#     targets = collections.defaultdict(list)
#     for a, b in sorted(tickets)[::-1]:
#         targets[a] += b,
#     route, stack = [], ['JFK']
#     while stack:
#         while targets[stack[-1]]:
#             stack += targets[stack[-1]].pop(),
#         route += stack.pop(),
#     return route[::-1]

class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """