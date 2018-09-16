import math

class Solution:

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        nsqrt = int(math.floor(math.sqrt(n)))
        squares = [i**2 for i in range(1, nsqrt+1)]

        q = [n]

        qn = []

        i = 1

        if n == 0: return 0

        while (True):
            while len(q) > 0:
                nc = q.pop()
                for sq in squares:
                    nn = nc-sq
                    if nn == 0:
                        return i
                    elif nn > 0:
                        qn.append(nn)
                    else:
                        break
            i+=1
            q = qn
            qn = []






if __name__ == '__main__':
    x = 12
    print(Solution().numSquares(x))