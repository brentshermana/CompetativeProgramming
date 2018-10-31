# https://leetcode.com/problems/container-with-most-water/

# solved! preprocess (nlogn) the leftmost and rightmost index of at least a given height,
# then get the best volume by iterating through each height (n).
#
# this problem was tricky! Required two 'passes' of preprocessing to get the info that was needed

class Solution:

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sorted_heights = sorted(height, reverse=True)  # high to low

        # could also replace this with a treemap, we are already sorted so nlogn here doesn't hurt
        height_to_index = {h: i for i, h in enumerate(height)}

        furthest_left = []
        furthest_right = []
        for _ in range(len(height)):
            # these assignments are acceptable because they are all guaranteed to be overwritten
            furthest_left.append(len(height))  # max + 1, rightmost
            furthest_right.append(-1)  # min - 1, leftmost

        # populate a discrete collection of preprocessed information:
        #   the rightmost and leftmost occurrence of a height
        for i, h in enumerate(height):
            h_i = height_to_index[h]
            if i < furthest_left[h_i]:
                furthest_left[h_i] = i
            if i > furthest_right[h_i]:
                furthest_right[h_i] = i

        # but really, we want to ask "what's the furthest right/left occurrence of a height
        #   greater than or equal to that height?"
        # TODO: rightmost_of_higher, leftmost_of_higher are confusing names.
        rightmost_of_higher = -1  # again, leftmost. will be overwritten on first iteration
        leftmost_of_higher = len(height) + 1  # again, rightmost. will be overwritten on first iteration
        for h in sorted_heights:
            h_i = height_to_index[h]

            rightmost_of_higher = max(rightmost_of_higher, furthest_right[h_i])
            furthest_right[h_i] = rightmost_of_higher

            leftmost_of_higher = min(leftmost_of_higher, furthest_left[h_i])
            furthest_left[h_i] = leftmost_of_higher

        # Now, used preprocessed information to get the best volume
        best_volume = -1
        for h, h_i in height_to_index.items():
            vol = h * (furthest_right[h_i] - furthest_left[h_i])
            if vol > best_volume:
                best_volume = vol

        return best_volume
