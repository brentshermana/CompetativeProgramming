from string import ascii_letters, digits
from collections import defaultdict

tokens = list(ascii_letters + digits)
tokens.sort()

# the input array contains only alphanumeric characters
# we're sort of doing radix sort, but there's only one 'radix'

# runtime is linear (n * size(letters, digits))

# because of the pop operations, space complexity is actually constant
def sort(arr):
    buckets = defaultdict(list)
    while len(arr) > 0:
        c = arr.pop()
        buckets[c].append(c)
    for token_class in tokens:
        bucket = buckets[token_class]
        while len(bucket) > 0:
            arr.append(bucket.pop())
    return arr
