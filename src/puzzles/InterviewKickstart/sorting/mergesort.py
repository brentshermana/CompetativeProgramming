
# 'mid' is the beginning of the second array
def merge(arr, base, mid, cap):
    new_arr = []
    a = base
    b = mid
    while a < mid and b < cap:
        # less than OR EQUALS is important for stability!!
        if arr[a] <= arr[b]:
            new_arr.append(arr[a])
            a += 1
        else:
            new_arr.append(arr[b])
            b += 1
    while a < mid:
        new_arr.append(arr[a])
        a += 1
    while b < cap:
        new_arr.append(arr[b])
        b += 1
    for i in range(len(new_arr)):
        arr[i+base] = new_arr[i]

def inner_merge_sort(arr, base, cap):
    if base + 1 >= cap:
        return
    mid = (base + cap) / 2
    inner_merge_sort(arr, base, mid)
    inner_merge_sort(arr, mid, cap)
    merge(arr, base, mid, cap)

def merge_sort(arr):
    inner_merge_sort(arr, 0, len(arr))
    return arr 


if __name__ == "__main__":
    print()