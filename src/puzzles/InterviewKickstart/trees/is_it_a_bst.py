import math

def validate(root, base_val, cap_val):
    if root is None:
        return True
    if not ( base_val < root.val < cap_val ):
        return False
    return validate(root.left_ptr, base_val, root.val) and \
           validate(root.right_ptr, root.val, cap_val)

# entry point
def isBST(root):
    return validate(root, -math.inf, math.inf)
