# SOLVED
# These kinds of problems take a lot of iteration
# logic... it would be worth considering how to efficiently
# handle that

def neighbors(r,c,board):
    for r, c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if r >= 0 and r < len(board) and c >= 0 and c < len(board[0]):
            yield r, c
    
def borders(board):
    for c in [0, len(board[0])-1]:
        for r in range(len(board)):
            yield r, c
    for r in [0, len(board)-1]:
        for c in range(len(board[0])):
            yield r, c
            
# flood-fill from the edges
def flood_fill(r, c, board, surrounded):
    stack = [(r, c)]
    while len(stack) > 0:
        r, c = stack.pop()
        # mark as not surrounded
        if board[r][c] == 'O' and surrounded[r][c]:
            surrounded[r][c] = False
            # add neighbors to stack
            for r, c in neighbors(r,c, board):
                # whether the neighbors are valid will be
                # checked later
                stack.append((r,c))
                        
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        
        # we can't avoid the linear space allocation
        # in general anyways due to flood-fill
        surrounded = []
        for row in board:
            surrounded.append([True]*len(row))
                 
        # just apply flood fill to the border
        for r, c in borders(board):
            flood_fill(r, c, board, surrounded)
            
        # finally, change all the O's that are surrounded to 'X'
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and surrounded[r][c]:
                    board[r][c] = 'X'