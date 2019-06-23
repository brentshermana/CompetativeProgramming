# The interesting part of this is that the set is 4 BILLION
# integers, in a file

# how would you do it with 1GB ram? 10 MB?

# approach 1: sort the file
#    ... how do you do this when you have less memory than the file size?
#    - perform a bunch of smaller sorts of your memory size, then merge them
#      all together. This works during the final merge because that merge is
#      from files into other files. These are disk operations, so memory usage
#      is limited.
#      To speed this up, dedicate whatever memory you have to buffering the
#      next k values from each file

# approach 2: process the integers as a stream and maintain a 4 billion bit
#             (500 mb) buffer, where a bit is flipped if we have seen that
#             particular value. After producing the filter, return the
#             number corresponding to the first bit that wasn't flipped
# (this only works for 1GB, as the filter takes 500 mb)

# NO CODE FOR THIS ONE