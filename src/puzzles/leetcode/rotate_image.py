# it's crazy that the solution to this can be 6 lines of code!
# this is one of the hardest problems I've solved because it's really not
# obvious how to:
#
# * handle the iteration over the starting points for odd square lengths
# * "flip" a val s.t. for a length of for example 5,
#   0<->4, 1<->3, 2<->2
#   that's the len(a)-1-r part
# ^^^ I think the flip part was really hard because it's a really uncommon
#     use case
# * identify the "flip then swap" pattern. at first I was writing out the
#   indexes incorrectly on my pet example and it ended up showing no pattern at all
#

class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # one of the bounds has to be rounded up, the other
        # needs to be rounded down. this is to ensure correctness
        # for odd lengths, and does not affect even lengths
        for r in range( (len(a)+1) // 2 ):
            for c in range( len(a) // 2 ):
                temp = a[r][c]
                # four rotations to go all the way around
                for _ in range(4):
                    # a rotation is equivalent to:
                    # "flip the row, then swap the row and col"
                    c, r = len(a)-1-r, c
                    # current location gets val from prev rotation
                    # next location gets this val
                    temp, a[r][c] = a[r][c], temp
