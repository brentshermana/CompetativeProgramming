import random
import copy

# sorts IN PLACE
def partition(l, base, cap):
    pivot = base # pivot around the leftmost value

    for i in range(base+1, cap):
        if l[i] <= l[base]:
            pivot += 1
            l[pivot], l[i] = l[i], l[pivot]
    l[base], l[pivot] = l[pivot], l[base] # put pivot value in middle

    return base,pivot,pivot+1,cap


def quicksort(l, base, cap):
    if cap - base <= 1:
        return

    b1, c1, b2, c2 = partition(l,base,cap)

    quicksort(l,b1,c1)
    quicksort(l,b2,c2)


if __name__ == "__main__":
    l = [i for i in range(20)]
    random.shuffle(l)
    l_original = copy.copy(l)
    quicksort(l, 0, len(l))

    [print("{:3d}   {:3d}".format(i,j)) for i,j in zip(l, l_original)]


