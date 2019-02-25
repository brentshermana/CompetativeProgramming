# Suppose we abstract our file system by a string in the following manner:
#
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
#
# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
#
# Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.
#
# Note:
# The name of a file contains at least a . and an extension.
# The name of a directory or sub-directory will not contain a ..
# Time complexity required: O(n) where n is the size of the input string.
#
# Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.


class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        long_len = 0 # longest path length seen so far
        lines = input.split('\n')
        len_at_indent = []
        for line in lines:
            indentation = line.count('\t')

            line_len = len(line) - indentation

            if len(len_at_indent) <= indentation:
                len_at_indent.append(line_len)
            else:
                del len_at_indent[indentation+1:] # get rid of higher indentation levels
                len_at_indent[indentation] = line_len

            if indentation >= 1: # add the size of the rest of the path
                len_at_indent[indentation] += len_at_indent[indentation-1]

            if '.' in line: # if it's a file, record the maximum path len
                # add the indentation because there are that many delimiters between path 'segments'
                long_len = max(long_len, len_at_indent[indentation] + indentation)

        return long_len

