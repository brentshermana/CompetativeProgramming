# this problem is trivial overall, but I got the 'nbits' calculation
# wrong on my first iteration. I need to memorize that formula!

# naive: generate every integer from 1 to N in binary, and perform a substring check
# clever alternatives?
#
# maybe we don't have to do a substring check for every integer in that range
# 7: 1, 10, 11, 100, 101, 110, 111
# categories: one bit, two bits, three bits
# observation: all one-bit values exist if all two bit values exist
# similarly, all two bit values exist if all three bit values exist

# I think we can solve this in s * log(n) time,
# by performing a loop at each position in s
# over the number of bits required to represent n (that's where the log comes from)
#
# for example, let's say we're at position i=4 of the binary string:
#
# 10110
#     ^
# ... and n is represented using 5 bits
# take the prev. n bits: 10110  ... and mark that value as 'present'
# take the prev n-1 bits 0110 ... and mark that value as 'present'
# etc...
# at the end, return whether every value has been marked as present

# I also think we can make this really efficient using bitwise operations...
# but I'm not sure how to right now

import math
class Solution:
    def queryString(self, binary: str, n: int) -> bool:
        # the number of bits needed to represent 'n'
        nbits = int(math.floor(math.log2(n))) + 1
        # note that we have index 0 in here, but we don't care about it since the
        # range we care about starts at '1'
        substring_present = [False for _ in range(n+1)]
        for i in range(len(binary)):
            val = 0
            for j in range(i, min(i+nbits, len(binary))):
                # bit shift (multiply by 2)
                val = val << 1
                # add the new bit if present
                if binary[j] == '1':
                    val += 1
                # mark the resulting val as present
                if val <= n:
                    substring_present[val] = True
        # all vals must be present
        return all(substring_present[i] for i in range(1, n+1))
