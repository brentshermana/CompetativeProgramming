import math

def binary_search(l, target, base=None, cap=None, i=None):
    if base == None:
        base = 0
    if cap == None:
        cap = len(l)
    if i == None:
        i = int(math.ceil((base+cap)/2))

    if base > cap: # base case
        return -1

    if l[i] == target:
        return i
    elif l[i] > target:
        # move left
        cap = i-1
    else:
        # move right
        base = i+1

    i = int(math.ceil(base+cap)/2)
    return binary_search(l, target, base, cap, i)


if __name__ == "__main__":
    x = 100

    l = []
    for i in range(x):
        l.append(i)

    for i in range(x):
        print(binary_search(l, i))
