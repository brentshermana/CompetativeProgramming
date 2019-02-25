# print the post-order values without recursion


def postorderTraversal(root):
    # each element: (node, state)
    # state 0: just entered stack
    # state 1: pushed left child
    # state 2: pushed right child
    if root is None:
        stack = []
    else:
        stack = [(root, 0)]

    while len(stack) > 0:
        node, state = stack.pop()

        if state == 0:
            state += 1
            if node.left_ptr is not None:
                stack.append((node, state))
                stack.append((node.left_ptr, 0))
                continue
        if state == 1:
            state += 1
            if node.right_ptr is not None:
                stack.append((node, state))
                stack.append((node.right_ptr, 0))
                continue
        if state == 2:
            print(node.val, end='')
            # only the final node doesn't have a space after it
            if len(stack) > 0:
                print(" ", end='')
