from search_test import test_first, test_last, test_found

def binarysearch(arr, target):
    lo = 0
    hi = len(arr)
    while (lo < hi):
        mid = lo + (hi - lo)//2
        if (arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            lo = mid + 1
        else: # arr[mid] < target
            hi = mid 
    if lo < len(arr) and arr[lo] == target:
        return lo
    return -1

# returns first occurence in the array
def binarysearch_first(arr, target):
    lo = 0
    hi = len(arr)
    while (lo < hi):
        mid = lo + (hi - lo)//2
        if arr[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    # case 1: target too high, so out of bounds
    if lo == len(arr):
        return -1
    # case 2: we're at the correct spot
    if arr[lo] == target:
        return lo
    # case 3: we're at the spot just before
    if arr[lo + 1] == target:
        return lo + 1
    # case 4: dne in array.
    return -1

# returns last occurence in the array
def binarysearch_last(arr, target):
    lo = 0
    hi = len(arr)
    while (lo < hi):
        mid = lo + (hi - lo)//2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    if (lo > 0 and arr[lo - 1] == target):
        return lo - 1
    return -1

if __name__ == "__main__":
    test_found(binarysearch)
    test_first(binarysearch_first)
    test_last(binarysearch_last)