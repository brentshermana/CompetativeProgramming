# https://leetcode.com/problems/merge-intervals/description/
#
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

# SUCCESS. My approach was just to allow the endpoints to refer to each other,
# sort them all, and accumulate an interval until the next node didn't intersect with
# it. This solution is nlogn due to the sort

left = 1
right = 2


class Node:
    def __init__(self, val, kind, other, l=None, r=None):
        self.other = other
        self.kind = kind
        self.val = val
        self.l = l
        self.r = r

    def linkr(self, r):
        self.r = r
        r.l = self

    def disconnect(self):
        if self.r != None:
            self.r.l = self.l
        if self.l != None:
            self.l.r = self.r
        self.l = None
        self.r = None


import math


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if len(intervals) == 0:
            return []

        nodes = []
        for i in intervals:
            nodes.append(Node(i.start, left, None))
            nodes.append(Node(i.end, right, nodes[-1]))
            nodes[-2].other = nodes[-1]

        # note that the values of 'kind' result in intervals which
        # 'overlap' only on their edge actually overlapping in this
        # list (that way it's not an edge case)
        nodes = sorted(nodes, key=lambda n: n.val + n.kind)

        # link the nodes into a dll
        head = nodes[0]
        current = nodes[1]
        head.linkr(current)
        for node in nodes[2:]:
            current.linkr(node)
            current = node

        ret = []

        lbound = head.val
        rbound = head.other.val

        while True:
            head = head.r

            if head == None:
                ret.append([lbound, rbound])
                return ret

            head.l.disconnect()  # let gc do its work

            if head.kind == right:  # we get info about right bounds from left counterparts
                continue
            elif head.val > rbound:  # nothing else will merge with the current interval
                ret.append([lbound, rbound])
                lbound = head.val
                rbound = head.other.val
            else:  # merge the current interval with this one
                rbound = max(rbound, head.other.val)
                head.other.disconnect()