# First, here's someone else's solution.
# It's much more concise than mine (C++)
# class Solution {
#  // author : s2003zy
#  // weibo : http://weibo.com/574433433
#  // blog : http://s2003zy.com
#  // Time : O(n)
#  // Space : O(1)
#  public:
#     int maxProduct(int A[], int n) {
#         int frontProduct = 1;
#         int backProduct = 1;
#         int ans = INT_MIN;
#         for (int i = 0; i < n; ++i) {
#             frontProduct *= A[i];
#             backProduct *= A[n - i - 1];
#             ans = max(ans,max(frontProduct,backProduct));
#             frontProduct = frontProduct == 0 ? 1 : frontProduct;
#             backProduct = backProduct == 0 ? 1 : backProduct;
#         }
#         return ans;
#     }
# };

# ^^^
# we're doing the same thing, but his logic is much simpler:
# - taking products from both sides doesn't have to be handled
#   in a special case: just do it anyways
# - handling zero values is actually really easy




# largest product  ~~ largest absolute value
# negative numbers sort of throw a wrench in any overly simple approach
# because you can't just throw them out. "valid" solutions can contain
# any even number of negative elements

# regarding zero: Should never be included

# SUCCESS
# each subarray which does not contain zeroes either has:
# 1: an even number of negative numbers: they cancel themselves out, so take the product of all of them
# 2: an odd number of negative numbers: we have to exclude one of them, so consider the products
# of all numbers until the last neg, and the product of all numbers after the first neg

# I'd be curious to see other solutions to this though...

def product(nums, base, cap):
    p = nums[base]
    for n in nums[base+1:cap]:
        p *= n
    return p

class Solution:
    
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # I don't think we even have to take this into account based on the problem constraints
        if len(nums) == 0:
            return 0
        
        # good starting value to handle edge cases (e.g. all zeroes)
        max_product = max(nums)
        
        # separating into subarrays that don't contain zero will simplify the rest of our
        # logic:
        sequences_without_zero = []
        seq = []
        for n in nums:
            if n == 0:
                if len(seq) > 0:
                    sequences_without_zero.append(seq)
                    seq = []
            else:
                seq.append(n)
        if len(seq) > 0:
            sequences_without_zero.append(seq)
            
        # take these sequences and operate on them
        for seq in sequences_without_zero:
            neg_indices = [i for i in range(len(seq)) if seq[i] < 0]
            
            candidate_products = [max_product]
            # odd number of negative indices: There are two possible subsequences
            # which could be the max
            if len(neg_indices) % 2 == 1:
                # sequence extending until last negative number
                if neg_indices[-1] > 0:
                    candidate_products.append(product(seq, 0, neg_indices[-1]))
                # sequence starting after first negative number:
                if neg_indices[0]+1 < len(seq):
                    candidate_products.append(product(seq, neg_indices[0]+1, len(seq)))
            else:
                # take the product of the entire range
                candidate_products.append(product(seq, 0, len(seq)))
                
            max_product = max(candidate_products)
                
        return max_product
        