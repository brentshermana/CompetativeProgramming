# I failed to solve this problem on my first attempt, and I even
# failed to correctly produce the recurrence relation formulation
#
# I think the key observation is that what uniquely identifies
# a subproblem is the current book you're looking at, as well as
# the state of the current shelf (which books are on it?)


# here's my SECOND draft of this problem, that I constructed using
# another leetcode solution as a reference:

# Discussion of the solution:
#
# We put the result of each calculation under the key 'index, current_width',
# which might be confusing because other 'carry-over' values passed by the caller
# go into the resulting value. Isn't it possible for the same i and current_width
# value to appear in different parts of the call tree with different 'current_height'
# values?
#
# It actually isn't! The reason for that is that the current book's predecessors must be books[x:i] for some x,
# and 'x' is actually represented uniquely by current_width for a given 'i'.
#
# Instead of (i, current_width), we could have actually used (i, x) as the key,
# or (i, num_predecessors_on_same_shelf), where num_predecessors = i-x
#
# current_width is just one approach that happens to be convenient

def dfs(books, shelf_width, cache, i, current_width, current_height):
    """
    returns the total height of the shelves containing this book and all other books to the right.

    This phrasing is deliberately precise: the height of the shelf containing this book can be affected
    by preceding books, which is why we need to pass 'current_height'
    """
    # base case: we don't have a "current" book, but we do have a current shelf,
    #            so return its height
    if i == len(books):
        return current_height

    # memoized subproblem
    # only the current width and the index affect the solutions to subproblems,
    # which is why we use them to form the key
    if (i, current_width) in cache:
        return cache[(i, current_width)]

    # explore the two possible decisions: should the book go on the current row,
    # or should we add it to a new row?

    # the current book is the start of a new shelf
    solution = current_height + dfs(books, shelf_width, cache, i+1, books[i][0], books[i][1])
    # add to current row if there's room
    if current_width + books[i][0] <= shelf_width:
        current_row_solution = dfs(books, shelf_width, cache, i+1, current_width+books[i][0], max(current_height, books[i][1]))
        solution = min(solution, current_row_solution)

    cache[(i, current_width)] = solution
    return solution


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        return dfs(books, shelf_width, {}, 0, 0, 0)


# here's my FIRST draft for this problem. It's correct,
# but exceeds the time limit because it doesn't use memoization
#
# I had a hard time knowing what to memoize on because there
# were so many state variables

def recurse(books, i, shelf_width, prev_shelves_height, cur_shelf_height, cur_shelf_width):
    if i == len(books):
        return prev_shelves_height + cur_shelf_height
    else:
        # starting a new_shelf with this book
        result = recurse(books, i+1, shelf_width, prev_shelves_height + cur_shelf_height, books[i][1], books[i][0])
        # adding this book to the current shelf (if possible)
        if books[i][0] + cur_shelf_width <= shelf_width:
            result = min(result, recurse(books, i+1, shelf_width, prev_shelves_height, max(cur_shelf_height, books[i][1]), cur_shelf_width+books[i][0]))
        return result

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        return recurse(books, 0, shelf_width, 0, 0, 0)
