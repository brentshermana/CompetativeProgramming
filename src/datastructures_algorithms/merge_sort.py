def merge(l,base, middle, cap):
    li = base
    hi = middle

    merged = []

    while li < middle or hi < cap:
        if li < middle and hi < cap:
            choose_low = l[li] < l[hi]
        elif li < middle:
            choose_low = True
        else:
            assert hi < cap
            choose_low = False

        if choose_low:
            merged.append(l[li])
            li += 1
        else:
            merged.append(l[hi])
            hi += 1

    l[base:cap] = merged



def merge_sort(l, base, cap):
    if cap - base <= 1:
        return

    middle = int((base+cap)/2)

    merge_sort(l,base,middle)
    merge_sort(l,middle,cap)

    merge(l,base,middle,cap)

if __name__ == "__main__":
    