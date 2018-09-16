"""
There is a box protected by a password. The password is n digits, where each letter can be one of the first k digits 0, 1, ..., k-1.

You can keep inputting the password, the password will automatically be matched against the last n digits entered.

For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.

Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.



Example 1:
Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.

Example 2:
Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
"""

class Solution:
    # FAIL I COULDNT FIGURE OUT HOW TO GET MINIMAL LENGTH
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        dp = set()

        prefix = ''.join(['0' for _ in range(n-1)])
        s = ''.join(['0' for _ in range(n-1)])

        ret_len = k**n + 2*(n-1)


        while True:
            orig_len = len(s)

            for d in range(k):
                if prefix + str(d) not in dp:
                    s += str(d)
                    dp.add(prefix + str(d))
                    prefix = prefix[1:] + str(d)
                    break

            if len(s) == orig_len or len(s) == ret_len:
                print("Len: {} Expected: {}".format(len(s), ret_len))
                return s

if __name__ == "__main__":
    print(Solution().crackSafe(int(input("n: ")), int(input("k: "))))

