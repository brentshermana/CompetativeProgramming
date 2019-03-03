# This problem's kind of stupid... oh well

# We're supposed to count the number of unique email addresses that are
# formed by a given list of email addresses, using a few rules:
#
# emails are of the form local@domain
#
# The following special rules apply to the local segment:
# - periods are ignored
# - everything after the + will be ignored
#
# This problem's really stupid, but we can take this opportunity to
# play around with prefix trees

from collections import defaultdict

class Node:
    def __init__(self):
        self.is_end = False
        self.succ = defaultdict(Node)

    def add(self, s, si=0):
        if si == len(s):
            self.is_end = True
        else:
            self.succ[s[si]].add(s, si+1)

    def __len__(self):
        l = sum( (len(n) for n in self.succ.values()) )
        if self.is_end:
            l += 1
        return l


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        prefix_tree = Node()
        for email in emails:
            local, domain = email.split('@')

            new_local = ""
            for c in local:
                if c == '+':
                    break
                elif c != '.':
                    new_local += c
            local = new_local

            email = '@'.join((local, domain))
            prefix_tree.add(email)
        return len(prefix_tree)