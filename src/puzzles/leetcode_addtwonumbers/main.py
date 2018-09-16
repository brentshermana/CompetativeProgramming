class Solution:

    def add(self, a, b):
        sum = a+b+self.carry
        if sum >= 10:
            sum -= 10
            self.carry = 1
        else:
            self.carry = 0
        return sum

    def getVal(self, a):
        if (a == None):
            return 0
        else:
            return a.val

    def iter(self, a):
        if (a == None):
            return None
        else:
            return a.next

    def addTwoNumbers(self, l1, l2):

        self.carry = 0
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ret = ListNode(self.add(l1.val, l2.val))

        l1 = self.iter(l1)
        l2 = self.iter(l2)

        current = ret

        while not (l1 == None and l2 == None and self.carry == 0):
            l1v = self.getVal(l1)
            l2v = self.getVal(l2)

            current.next = ListNode(self.add(l1v, l2v))
            current = current.next

            l1 = self.iter(l1)
            l2 = self.iter(l2)

        return ret