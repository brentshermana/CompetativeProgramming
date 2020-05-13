# worth looking over, the dp formulation wasn't obvious

# observation: negative numbers "flip" the product to be negative
# * two negative numbers is good! it means they flip back
# other observation: zero is a hard boundary -- no point in considering elements on both sides
# of a zero, only one side will matter

# f(i) <- largest product whose right side is this position
# f(i) = max(f(i-1) * a(i), a(i))
#
# this doesn't work because a running product can go negative for awhile, then go positive after
# seeing another negative number
#
# hi(i) <- largest product whose right side is this position
# hi(i) = max(hi(i-1) * a(i), a(i), lo(i-1) * a(i))
# lo(i) <- lowest product whose right side is this position
# lo(i) = min(hi(i-1) * a(i), a(i), lo(i-1) * a(i))



class Solution:
    def maxProduct(self, a: List[int]) -> int:
        hi = [a[0]]
        lo = [a[0]]
        for i in range(1, len(a)):
            vals = [hi[i-1]*a[i], lo[i-1]*a[i], a[i]]
            hi.append(max(vals))
            lo.append(min(vals))
        return max(hi)
