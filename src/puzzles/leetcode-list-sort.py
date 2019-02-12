# SOLVED with merge sort
# in this case, merge sort is in-place due to linked list properties

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def llen(l):
    count = 0
    while l is not None:
        l = l.next
        count += 1
    return count

def split(l):
    length = llen(l)
    start = l
    mid = start
    for _ in range( (length-1) // 2): # <-- not having the -1 causes an error!
        mid = mid.next
    start2 = mid.next
    # disconnect the end of the first from the start of the next
    mid.next = None
    return start, start2

def take_from(takes, taken):
    takes.next = taken # connect
    takes = takes.next # advance
    taken = taken.next # advance
    takes.next = None  # disconnect
    return takes, taken

def merge(a, b):
    sentinel = ListNode(None)
    n = sentinel
    while a is not None and b is not None:
        if a.val < b.val:
            n, a = take_from(n, a)
        else:
            n, b = take_from(n, b)
    # only one of these branches will be hit
    if a is not None:
        n.next = a
    if b is not None:
        n.next = b
    return sentinel.next
    

def mergeSort(l):
    length = llen(l)
    if length < 2:
        return l
    a, b = split(l)
    a = mergeSort(a)
    b = mergeSort(b)
    return merge(a, b)

class Solution:
    def sortList(self, head: 'ListNode') -> 'ListNode':
        return mergeSort(head)