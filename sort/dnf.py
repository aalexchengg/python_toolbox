
def sort(arr):
    def swap(arr, i ,j):
        arr[i], arr[j] = arr[j], arr[i]
    n = len(arr)
    lo = 0
    mid = 0
    hi = n - 1
    while (mid <= hi):
        if arr[mid] == 0:
            swap(lo, mid)
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            swap(mid, hi)
            hi -= 1
    return arr
