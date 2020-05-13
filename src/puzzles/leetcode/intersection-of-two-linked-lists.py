
# this is not my solution, but I was really impressed with it!
# it requires running through each list twice but it's really clever

# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/550227/Java-1ms-recursion


# my solution is ok, it runs in n+m time (length of the two lists)
# but requires two passes:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def get_length(n):
    l = 0
    while n is not None:
        n = n.next
        l += 1
    return l

class Solution:
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> ListNode:
        a_len = get_length(a)
        b_len = get_length(b)

        # "synchronize" the head nodes, such that the resulting lists are the same length
        # ( guaranteeing they will converge )
        if a_len > b_len:
            for _ in range(a_len-b_len):
                a = a.next
        else:
            for _ in range(b_len-a_len):
                b = b.next

        # advance together until we get reference equality, or we reach the end of the lists
        while a is not b and a is not None and b is not None:
            a = a.next
            b = b.next

        return a
