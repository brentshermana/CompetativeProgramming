# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# The real challenge here is capturing the recursive "state"

# for a standard order traversal,
# each node is visited at most X times:
# first time: yield from left
# second time: yield it
# third time: yield from right
# fourth time: mark as "expended"


# SUCCESS... Although another person had a simple solution: There is no
# need to store an explicit state...



# class BSTIterator(object):
#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.stack = []
#         curr = root
#         while curr is not None:
#             self.stack.append(curr)
#             curr = curr.left
            
#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return bool(self.stack)

#     def next(self):
#         """
#         :rtype: int
#         """
#         curr = self.stack.pop()
#         val = curr.val
#         if curr.right:
#             curr = curr.right
#             while curr:
#                 self.stack.append(curr)
#                 curr = curr.left
#         return val

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # each stack element is (node, state)
        self.node_stack = [root]
        self.state_stack = [1]
        if root == None:
            self.node_stack.pop()
            self.state_stack.pop()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        self.goto_next()
        return len(self.state_stack) > 0

        
    # adjusts the stack to be equal to the "next" node
    def goto_next(self):
        while len(self.node_stack) > 0:
            state = self.state_stack[-1]
            node = self.node_stack[-1]

            if state == 1:
                self.state_stack[-1]+=1
                if node.left != None:
                    self.state_stack.append(1)
                    self.node_stack.append(node.left)
            elif state == 2:
                return
            elif state == 3:
                self.state_stack[-1]+=1
                if node.right != None:
                    self.state_stack.append(1)
                    self.node_stack.append(node.right)
            else:
                self.state_stack.pop()
                self.node_stack.pop()


    def next(self):
        """
        :rtype: int OR NONE IF NOTHING NEXT
        """
        self.goto_next()

        self.state_stack[-1] += 1
        return self.node_stack[-1].val

        


        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())