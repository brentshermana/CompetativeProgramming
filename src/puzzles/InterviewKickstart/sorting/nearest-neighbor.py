# Given a point P, and another N points in 2D space, find K points
# out of the N points which are nearest to P

from heapq import heapify, heappop

# we're assuming that a and b are both 2-tuples
def euclidean(a, b):
    return sqrt(sum([abs(x-y) ** 2 for x, y in zip(a, b)]))

def find_nearest_neighbours(px, py, others, k):
    p = (px, py)
    heap = [(euclidean(p, point), point) for point in others]
    heapify(heap)
    return [heappop(heap)[1] for _ in range(k)]
