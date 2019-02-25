# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.

# DONE easy dfs with backtracking

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        d2c = {'2' :'abc', '3' :'def', '4' :'ghi', '5' :'jkl', '6' :'mno', '7' :'pqrs', '8' :'tuv', '9' :'wxyz'}
        def rec(d2c, ret, digits, l, i):
            for next_c in d2c[digits[i]]:
                l.append(next_c)
                if len(l) == len(digits):
                    ret.append(''.join(l))
                else:
                    rec(d2c, ret, digits, l, i+1)
                l.pop()

        ret = []
        rec(d2c, ret, digits, [], 0)
        return ret