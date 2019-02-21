# FAILED. I couldn't get this one correct by myself.

## here is the first solution I came up with. It's way too slow:
class Solution:
    def canPartitionKSubsets(self, nums: 'List[int]', k: 'int') -> 'bool':
        subset_target = sum(nums) / k

        def rec(nums_i, num_sets, cur_sum):
            if nums_i == len(nums):
                # if the current set sum is zero, either the current
                # set is empty, or it could be added to any of our sets
                # without changing their sums
                return num_sets == k and cur_sum == 0
            else:
                # try adding each element in the remainder of the array to this set
                for i in range(nums_i, len(nums)):
                    # swap selected element to front
                    nums[nums_i], nums[i] = nums[i], nums[nums_i]

                    new_sum = cur_sum + nums[nums_i]
                    complete_set = new_sum == subset_target
                    if complete_set:
                        if rec(nums_i+1, num_sets+1, 0):
                            return True
                    else:
                        if rec(nums_i+1, num_sets, new_sum):
                            return True
                    # swap back
                    nums[nums_i], nums[i] = nums[i], nums[nums_i]
                return False

        return rec(0, 0, 0)

# ^^^ analysis of the code: The time complexity would be O(n!)
# the first recursive call would make n recursive calls, each of which
# would have n-1 recursive calls, etc.




# here's a strong solution:
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/140541/Clear-explanation-easy-to-understand-C++-:-4ms-beat-100
# he points out that "for each bucket, try all possible content"  is O(k*2^n).
# I'm not convinced that's the upper bound an implementation which ensures each bucket's subset does not
# intersect with another bucket's subset would have, but it's at least a good ballpark approximation

# The solution he actually provides is O(k^n). We can reason about this easily using the formula
# tree_size = b^h - 1
# we're branching on 'k', because we're recursing on each bucket (aka sums), and the solution is
# only complete once we have allocated all n of our values
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        sums = [0]*k
        subsum = sum(nums) / k
        nums.sort(reverse=True)
        l = len(nums)

        def walk(i):
            if i == l:
                return len(set(sums)) == 1
            for j in xrange(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and walk(i+1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False

        return walk(0)
