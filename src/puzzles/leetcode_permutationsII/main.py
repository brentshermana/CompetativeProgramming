# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


# SOLVED. The real solution here was in preventing duplicates by sorting the nodes
#         and using a dll to avoid much more costly list operation

class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None


class Dll:
    def __init__(self):
        self.l = None
        self.r = None
        self.size = 0

    def pushr(self, val):
        n = Node(val)
        if self.size == 0:
            self.l = n
            self.r = n
        else:
            # link n and self.r
            n.l = self.r
            self.r.r = n
            # n is new self.r
            self.r = n
        self.size += 1

    def pushl(self, val):
        n = Node(val)
        if self.size == 0:
            self.l = n
            self.r = n
        else:
            # link n and self.l
            n.r = self.l
            self.l.l = n
            # n is new self.l
            self.l = n
        self.size += 1

    def popl(self):
        n = self.l
        if (self.size > 1):
            n.r.l = None  # node right of n forgets n
            self.l = n.r  # ... and becomes new l
            n.r = None  # n also forgets neighbor
        self.size -= 1
        return n.val

    def list(self):
        ret = []
        temp = self.l
        while temp != None:
            ret.append(temp.val)
            temp = temp.r
        return ret


class Solution:
    # iterates thru the *dlls* containing each unique permutation!
    def permuteUniqueDll(self, nums):
        if nums.size == 1:
            yield nums
        else:
            last_popped = None
            for _ in range(nums.size):
                pop = nums.popl()
                if pop == last_popped:
                    pass  # don't recurse, would just be giving duplicates
                else:
                    # iterate through permutations formed by
                    # the remaining nums.
                    for permuted_rest in self.permuteUniqueDll(nums):
                        permuted_rest.pushl(pop)
                        yield permuted_rest
                        permuted_rest.popl()
                nums.pushr(pop)  # push to the right what was popped from left === rotation
                last_popped = pop

    # entry point to solution
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # perform an initial sort, so that duplicates
        # are next to each other:
        nums.sort()
        # next, convert to Dll
        dll = Dll()
        for num in nums:
            dll.pushr(num)
        # finally, delegate to Dll method
        return [p.list() for p in self.permuteUniqueDll(dll)]
