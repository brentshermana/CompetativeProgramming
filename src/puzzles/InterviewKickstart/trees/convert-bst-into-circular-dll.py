# convert a binary search tree into a circular doubly linked list
# after the conversion, left_ptr === "previous", and right_ptr === "next",
# where the list is fully sorted from low to high
# highest_node.right_ptr should point to the lowest element, and
# lowest_node.left_ptr should point to the highest element

def rec(node):
    # call children. They will each return the lowest node they've seen and the highest
    if node.left_ptr is not None:
        leftmost, highest_to_left = rec(node.left_ptr)
        node.left_ptr = highest_to_left
        highest_to_left.right_ptr = node
    else:
        leftmost = node

    if node.right_ptr is not None:
        lowest_to_right, rightmost = rec(node.right_ptr)
        node.right_ptr = lowest_to_right
        lowest_to_right.left_ptr = node
    else:
        rightmost = node

    return leftmost, rightmost


def BSTtoLL(root):
    if root is not None:
        leftmost, rightmost = rec(root)
        # create the final circular link
        rightmost.right_ptr = leftmost
        leftmost.left_ptr = rightmost
        return leftmost
    else:
        return None
