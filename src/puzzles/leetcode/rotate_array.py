# not my solution, much cleaner + clever: use reverse operations.
class Solution:
    def rotate(self, a, k):
        # make sure k lies on the array
        k %= len(a)
        # full reverse. this correctly partitions the elements into the first k,
        # and then the rest, but they're out of order within those partitions
        self._reverse(a, 0, len(a) - 1)
        # reversing each partition separately restores the desired order
        self._reverse(a, 0, k - 1)
        self._reverse(a, k, len(a) - 1)

    def _reverse(self, a, lo, hi):
        """ hi is inclusive """
        right_mid = lo + (hi - lo + 1) // 2
        for i in range(lo, right_mid):
            self._swap(a, i, hi + lo - i)

    def _swap(self, a, i, j):
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp


# my solution: linear time, o(1) space, but not cache_friendly
# the core idea is that you should just hold a single temp var and keep swapping
# to wherever the temp var goes
class Solution:
    def rotate(self, a: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k % len(a) == 0:
            # no work needed
            return
        if len(a) <= 1:
            return

        swaps = 0
        # the need for this outer 'start_i' loop is kinda weird. the inner while,
        # for the following k values and len(a)==6, ends up swapping every x-th val, as follows:
        # k=1, x=1 ( all are swapped )
        # k=2, x=2 ( every other val is swapped )
        # k=3, x=3 ( every third val is swapped )
        # k=4, x=2 ( every other val is swapped )
        # k=5, x=1 ( all are swapped )
        #
        # ... so what's the trend? I couldn't figure it out, but I did observe that the pattern is
        #     always "every x-th val is swapped", so for example if it's every other val
        #     you can start at x=0 and x=1 and then everything's done!

        for start_i in range(len(a)):
            if swaps == len(a):
                # all done!
                return
            i = start_i
            temp = a[start_i]
            while True:
                # the location where a[i] belongs
                j = (i + k) % len(a)
                # need to hold the val at j because we'll overwrite it
                temp2 = a[j]
                a[j] = temp
                temp = temp2
                swaps += 1
                # on the next iteration, write the new temp to the new location
                i = j

                # we'll have swapped everything for this loop when i == start_i again
                if i == start_i:
                    break
