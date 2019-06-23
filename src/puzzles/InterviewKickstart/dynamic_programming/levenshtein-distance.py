# given two words a and b, find the minimum number of steps required to convert a to b
# Here are the operations:
# - insert a character
# - delete a character
# - replace a character

# solution: create a 2d table where one dimension is as long as one of the words, and
# the other dimension is as long as the other word. (with + 1 adjustments). Track the 

from math import inf

def  levenshteinDistance(a, b):
    # edge case: empty strings
    if len(a) == 0 or len(b) == 0:
        return abs(len(a)-len(b))

    # we need the +1 adjustment because the first position corresponds to the position
    # immediately before consuming a character from either string
    table = []
    for _ in range(len(a)+1):
        table.append([0] * (len(b)+1))

    # abstract out out-of-bounds cases
    def cell(i, j):
        if i >= 0 and j >= 0:
            return table[i][j]
        else:
            return inf

    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0 and j == 0:
                # the first cell is 0
                continue
            # These options represent either an insertion or a deletion
            successors = [cell(i-1, j) + 1,
                          cell(i, j-1) + 1]

            if a[i-1] == b[j-1]:
                # because the characters line up, there's no cost
                # to consuming them together
                successors.append(cell(i-1, j-1))
            else:
                # because the characters don't line up, this represents
                # the cost of changing one of the characters to the other
                successors.append(cell(i-1, j-1)+1)

            table[i][j] = min(successors)

    return table[len(a)][len(b)]
