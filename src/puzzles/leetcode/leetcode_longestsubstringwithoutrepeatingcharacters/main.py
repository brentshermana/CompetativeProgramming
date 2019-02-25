class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        base = 0
        cap = 0

        ins = set()

        while cap < len(s):
            if s[cap] in ins:
                # must "reset" the count
                while s[cap] in ins:
                    ins.remove(s[base])
                    base += 1
                ins.add(s[cap])
                cap += 1
            else:
                # add the new char to the set
                ins.add(s[cap])
                cap += 1

            m = max(m, cap-base)

        return m