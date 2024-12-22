from search_test import test_first, test_last

# returns first occurence in the array
def binarysearch_first(arr, target):
    low, high = 0, len(arr)-1
    first = -1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            first = mid
            high = mid - 1

        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return first

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
    test_first(binarysearch_first)
    test_last(binarysearch_last)