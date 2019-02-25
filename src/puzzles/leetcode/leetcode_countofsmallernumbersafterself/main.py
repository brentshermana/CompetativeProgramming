# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
#
# Example:
#
# Input: [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.


# damnit I ran out of time! Most of the time my solution gives the correct answer, but for certain values
# my output will be one higher than it should be... no idea what the bug is

class Node:
    def __init__(self, val):
        self.val = val
        self.treesize = 1
        self.left = None
        self.right = None

    def leftsize(self):
        if self.left == None:
            return 0
        else:
            return self.left.treesize


class Tree:
    def __init__(self):
        self.root = None

    # also returns the number of values in the tree which are lower than val
    def add(self, val):
        if self.root == None:
            self.root = Node(val)
            return 0
        else:
            smaller = 0

            n = self.root
            while True:
                n.treesize += 1

                if n.val == val:
                    return smaller + n.leftsize()
                elif n.val < val:  # go right
                    if n.right == None:
                        n.right = Node(val)
                        return smaller + n.leftsize() + 1
                    else:
                        smaller += n.leftsize() + 1
                        n = n.right
                else:  # go left
                    if n.left == None:
                        n.left = Node(val)
                        return smaller
                    else:
                        n = n.left


class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t = Tree()
        counts = []
        for num in reversed(nums):
            counts.append(t.add(num))

        return list(reversed(counts))

print(Solution().countSmaller([5,2,6,1]))