# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.



# TOOK A LONG TIME TO COME UP WITH THE SOLUTION BECAUSE I WASN'T WILLING TO THINK ABOUT BRUTE FORCE
# AND WANTED TO SKIP STRAIGHT TO THE SOLUTION. STUPID



# N^4 solution: iterate through every four points and see if they form a rectangle. track the smallest volume

# N^3 solution: iterate through every three points and see if they could form a rectangle. search a hash set for the fourth such point in constant time

# N^2 solution: iterate through every pair of points and see if they are OPPOSITE points (they have neither their x nor their y in common). search a hash
#               set for the other two points in constant time
import math
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        minArea = math.inf
        # we want fast searches
        points_set = set([tuple(p) for p in points])
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points[i+1:]):
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    area = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                    if area < minArea:
                        p3 = (p1[0], p2[1])
                        p4 = (p2[0], p1[1])
                        if p3 in points_set and p4 in points_set:
                            minArea = area

        if minArea == math.inf:
            return 0
        else:
            return minArea
