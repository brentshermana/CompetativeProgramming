# The question asks for three non-overlapping intervals with maximum sum of all 3 intervals. If the middle interval is [i, i+k-1], where k <= i <= n-2k, the left interval has to be in subrange [0, i-1], and the right interval is from subrange [i+k, n-1].
#
# So the following solution is based on DP.
#
# posLeft[i] is the starting index for the left interval in range [0, i];
# posRight[i] is the starting index for the right interval in range [i, n-1];
# Then we test every possible starting index of middle interval, i.e. k <= i <= n-2k, and we can get the corresponding left and right max sum intervals easily from DP. And the run time is O(n).
#
# Caution. In order to get lexicographical smallest order, when there are two intervals with equal max sum, always select the left most one. So in the code, the if condition is ">= tot" for right interval due to backward searching, and "> tot" for left interval. Thanks to @lee215 for pointing this out!
#
# C++:
#
# class Solution {
# public:
#     vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
#         int n = nums.size(), maxsum = 0;
#         vector<int> sum = {0}, posLeft(n, 0), posRight(n, n-k), ans(3, 0);
#         for (int i:nums) sum.push_back(sum.back()+i);
#        // DP for starting index of the left max sum interval
#         for (int i = k, tot = sum[k]-sum[0]; i < n; i++) {
#             if (sum[i+1]-sum[i+1-k] > tot) {
#                 posLeft[i] = i+1-k;
#                 tot = sum[i+1]-sum[i+1-k];
#             }
#             else
#                 posLeft[i] = posLeft[i-1];
#         }
#         // DP for starting index of the right max sum interval
#         // caution: the condition is ">= tot" for right interval, and "> tot" for left interval
#         for (int i = n-k-1, tot = sum[n]-sum[n-k]; i >= 0; i--) {
#             if (sum[i+k]-sum[i] >= tot) {
#                 posRight[i] = i;
#                 tot = sum[i+k]-sum[i];
#             }
#             else
#                 posRight[i] = posRight[i+1];
#         }
#         // test all possible middle interval
#         for (int i = k; i <= n-2*k; i++) {
#             int l = posLeft[i-1], r = posRight[i+k];
#             int tot = (sum[i+k]-sum[i]) + (sum[l+k]-sum[l]) + (sum[r+k]-sum[r]);
#             if (tot > maxsum) {
#                 maxsum = tot;
#                 ans = {l, i, r};
#             }
#         }
#         return ans;
#     }
# };

def subseqSums(nums, k):
    cur_sum = sum(nums[:k])
    sums = [cur_sum]

    for i in range(k, len(nums)):
        cur_sum -= nums[i-k]
        cur_sum += nums[i]

        sums.append(cur_sum)

    return sums

class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sums = subseqSums(nums, k)

        leftbest = [0] * len(sums) # array of the index of the best subsequence at or to the left
        # of the given index
        for i in range(1, len(sums)-2*k):
            leftbest[i] = max([leftbest[i-1],i], key=sums.__getitem__)

        # same thing for right ranges
        rightbest = [0] * len(sums)
        rightbest[len(sums)-1] = len(sums)-1
        for i in range(len(sums)-2, 2*k-1, -1):
            rightbest[i] = max([i,rightbest[i+1]], key=sums.__getitem__)

        best = None
        best_sum = -1

        # now iterate through possible middle ranges
        for i in range(k, len(sums)-k):
            current_sum = sums[i] + sums[leftbest[i-k]] + sums[rightbest[i+k]]
            if current_sum > best_sum:
                best_sum = current_sum
                best = [leftbest[i-k], i, rightbest[i+k]]

        return best


