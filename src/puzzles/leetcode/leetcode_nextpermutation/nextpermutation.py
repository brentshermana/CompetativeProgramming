# OFFICIAL PROMPT

# Implement next permutation, which rearranges numbers into the lexicographically next
# greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1



# MY DISCUSSION:

# ALL permutations can be generated easily using a recursive algorithm, which necessarily takes LINEAR space.

# The fact that we can only use constant space implies that we should be able to accomplish this
# just using swaps

# larger permutations are achieved by swapping a small number on the left with a larger number on the right


# naive: swap the rightmost value with the first one to the left that is less than it
# - problem: there may not be *any* less than it
# - problem: Even if there is a lesser digit to the left, it may be all the way to the left.
#            We'd be increasing the value by too much rather than getting the next largest one

# Essentially, what this problem is asking for is an "online" version of the problem "print out all permutations
#   in order from lowest to highest"

# Here is a simple permutation generator:

# from collections import deque
# def permutations(nums):
#   if len(nums) <= 1:
#       yield nums
#   else:
#       for _ in range(len(nums)):
#           # will be the prefix
#           front = nums.popleft()
#           for per in permutations(nums):
#               per.appendleft(front)
#               yield per
#               per.popleft()
#           # rotate
#           nums.append(front)
# def printPermutations(nums):
#   for p in permutations(deque(nums)):
#       print(p)

# Implement next permutation, which rearranges numbers into the lexicographically next
# greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# ALL permutations can be generated easily using a recursive algorithm, which necessarily takes LINEAR space.

# The fact that we can only use constant space implies that we should be able to accomplish this
# just using swaps

# larger permutations are achieved by swapping a small number on the left with a larger number on the right


# naive: swap the rightmost value with the first one to the left that is less than it
# - problem: there may not be *any* less than it
# - problem: Even if there is a lesser digit to the left, it may be all the way to the left.
#            We'd be increasing the value by too much rather than getting the next largest one

# Essentially, what this problem is asking for is an "online" version of the problem "print out all permutations
#   in order from lowest to highest"

# Here is a simple permutation generator:

# from collections import deque
# def permutations(nums):
#   if len(nums) <= 1:
#       yield nums
#   else:
#       for _ in range(len(nums)):
#           # will be the prefix
#           front = nums.popleft()
#           for per in permutations(nums):
#               per.appendleft(front)
#               yield per
#               per.popleft()
#           # rotate
#           nums.append(front)
# def printPermutations(nums):
#   for p in permutations(deque(nums)):
#       print(p)

# Unfortunately it doesn't do the sort of thing we're looking for....
# maybe it's just easier to work through an example:

# The answer to this problem is
# 1 3 5 8 9 7 6 4 2 <- step 1: find the rightmost position that has a value larger than it to its left, then
#                              swap them (specifically, with the number that is smallest among the largers)
# 1 3 5 8 2 4 6 7 9 <- step 2: sort all numbers to the right of the swap position from low to high,
#                              effectively reducing the value as much as possible while keeping it above the original
#   

# another observation: We have to know, at the first sight of a decrease when moving right to left, which element is
#                   the least among those that are greater. This query is really cheap if we have the other elements
#                   pre-sorted, which we can do with insertion sort. Each time we move to the left, we're "inserting"
#                   that element into the set to its right... However this is N^2 worst case.
#
# So it's probably better to use quicksort or merge sort. HOWEVER these are not constant space, due to the memory
# cost of recursion. So insertion sort is the way to go.


# SUCCESS

class Solution:
    def insertionSort(self, nums, leftmost_i):
        val = nums[leftmost_i]
        for i in range(leftmost_i+1, len(nums)):
            if nums[i] >= val:
                nums[i-1] = val
                return
            else:
                nums[i-1] = nums[i]
        # if we haven't returned, then val belongs at the rightmost position
        nums[-1] = val

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        leftmost_i = len(nums)-2
        for leftmost_i in range(len(nums)-2, -1, -1):# from len(nums-2) through zero by -1
            if nums[leftmost_i] < nums[-1]:# the element to the right is always the largest

                # find the smallest number to the right that is greater than this one,
                swap_i = len(nums)-1
                while swap_i > leftmost_i+1 and nums[swap_i-1] > nums[leftmost_i]:
                    swap_i -= 1

                # then swap them
                temp = nums[leftmost_i]
                nums[leftmost_i] = nums[swap_i]
                nums[swap_i] = temp

                # finally, sort the range [leftmost_i+1, len(nums)-1], effectively making it 
                # as small as possible while still being larger than the previous permutation
                # - Note that this range is already sorted, except for index swap_i
                # ^^^ ... although, because of the way we've been incrementally sorting all along,
                #         this step is taken care of automatically!

                break # ... so we're done.
            else:
                self.insertionSort(nums, leftmost_i)
        # once the loop breaks, we've either sorted the list or found the permutation!








