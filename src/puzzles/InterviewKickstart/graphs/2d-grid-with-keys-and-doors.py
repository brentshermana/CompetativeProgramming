# find the shortest path on a 2D grid that represents a maze-like area,
# a start cell, and a goal cell. You can go up, down, left, or right.
# each cell in the grid is land, water, door, or key
# Each type of key will open only one type of door, but can be used multiple
# Times.

# For this problem, we can assume there will always be a path

# YOU CAN VISIT A CELL MULTIPLE TIMES

# cell specifications:
# '#' - water
# '.' - land
# <lowercase letter> - key
# <uppercose letter> - door
# '@' - starting cell
# '+' - ending cell


# I relied on a few optimizations/observations for this solution
# 1) Theere ore only 10 types of keys, so we can use BITSETS
# 2) we can revisit a tile, so rather than checking if we've visited
#    a coord, we must check if we have visited a coord with a superset of
#    the current keys, with the observation being that if you're introducing
#    a unique superset, you can visit 
# 3) backpointers must also be done on a per-coordinate and keyset
#    combination



from collections import deque, defaultdict

# Because the set of possible keys is small, we should use a bitset
# for constant time operations:
# This class is IMMUTABLE
class CharBitSet:
    @staticmethod
    def copy(s):
        new_s = CharBitSet()
        # primitive copy is ok
        new_s.bitset = s.bitset
        return new_s

    def __init__(self):
        self.bitset = int()

    def contains(self, l):
        l = l.lower()
        l_bit = 1 << (ord(l) - ord('a'))
        return l_bit & self.bitset == l_bit

    def add(self, l):
        l = l.lower()
        if self.contains(l):
            return self
        else:
            copy = CharBitSet.copy(self)
            copy.bitset = copy.bitset | (1 << (ord(l) - ord('a')))
            return copy

    def is_subset_of(self, other):
        return (self.bitset & other.bitset) == self.bitset

    def __hash__(self):
        return self.bitset

    def __eq__(self, x):
        try:
            return self.bitset == x.bitset
        except:
            return False

    def __str__(self):
        return str(self.bitset)
    def __repr__(self):
        return self.__str__()

def adj(grid, r, c, keyset, visited, bp):
    for dr, dc in ((0,1),(0,-1),(-1,0),(1,0)):
        pos = new_pos(grid, dr+r, dc+c, keyset, visited)
        if pos is not None:
            # print("BP {} = {}".format(pos, (r, c, keyset)))
            assert pos not in bp
            bp[pos] = (r, c, keyset) 
            yield pos

def is_visited(r,c,keyset,visited):
    # print("> is visited... {}, {}, {}".format(r, c, keyset))
    for ks in visited[r][c]:
        if keyset.is_subset_of(ks):
            #print("    YES for {}".format(ks))
            return True
        # else:
        #     print("    ... not for {}".format(ks))
    visited[r][c].append(keyset)
    return False


def new_pos(grid, r, c, keyset, visited):
    if not in_bounds(grid, r, c):
        return None

    floor = grid[r][c]
    if floor == '#': # water
        return None
    if floor in '@+.': # always traversible
        if not is_visited(r, c, keyset, visited):
            return r, c, keyset
        return None
    if floor.islower(): # it's a key
        # this was tough to debug... we have to check if the space was
        # visited by what the keyset WILL be, to make sure its immediate
        # successors aren't able to go right back to it
        if not is_visited(r, c, keyset.add(floor), visited):
            return r, c, keyset.add(floor)
        return None
    # it's a door:
    if keyset.contains(floor) and not is_visited(r, c, keyset, visited):
        return r, c, keyset
    return None

def path(r, c, keyset, bp):
    p = []
    while r != -1:
        p.append([r, c])
        r, c, keyset = bp.get((r, c, keyset), (-1, -1, -1))
    p.reverse()
    return p


def in_bounds(grid, r, c):
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

def find_shortest_path(grid):
    # setup: initialize the 'visited' set,
    #        find the start and end points
    q = deque()
    visited = [] # a 3D array: r, c, list of charbitsets
    bp = {} # (r, c, keyset) -> prev (r, c, keyset)
    for r, row in enumerate(grid):
        visited.append([[] for _ in range(len(row))])
        for c, elem in enumerate(row):
            if elem == '+':
                end = (r, c)
            if elem == '@':
                visited[r][c].append(CharBitSet())
                q.appendleft((r, c, CharBitSet()))

    while True:
        r, c, keyset = q.pop()
        if (r, c) == end:
            return path(r, c, keyset, bp)
        for a in adj(grid, r, c, keyset, visited, bp):
            q.appendleft(a)

grid = ["a.A+",
        "@..A"]
print(find_shortest_path(grid))



