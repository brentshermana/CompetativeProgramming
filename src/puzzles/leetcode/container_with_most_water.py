# greedy strategy?
# moving the higher edge in will NEVER increase the area

# I couldn't identify this as a greedy strategy problem and had to look at a hint

class Solution:
    def maxArea(self, a: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(a)-1
        while l < r:
            area = min(a[l], a[r]) * (r - l)
            max_area = max(max_area, area)
            if a[l] > a[r]:
                r -= 1
            else:
                l += 1
        return max_area
