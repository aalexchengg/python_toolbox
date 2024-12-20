# author: abcheng
from sort_tests import test

# O(nlogn), stable, not in place

def sort(arr: list):
    # merge algorithm
    def merge(arr, lo, mid, hi):
        sorted_arr = []
        left_pointer = lo
        right_pointer = mid
        while (left_pointer < mid and right_pointer < hi):
            if arr[left_pointer] < arr[right_pointer]:
                sorted_arr.append(arr[left_pointer])
                left_pointer += 1
            else:
                sorted_arr.append(arr[right_pointer])
                right_pointer += 1
        while (left_pointer < mid):
            sorted_arr.append(arr[left_pointer])
            left_pointer += 1
        while (right_pointer < hi):
            sorted_arr.append(arr[right_pointer])
            right_pointer += 1
        for i, num in enumerate(sorted_arr):
            arr[lo + i] = num
    # mergesort algorithm
    def mergesort(arr, lo, hi):
        # lo is inclusive, hi is exclusive
        if hi - lo <= 1 :
            return arr
        midpoint = (hi + lo)//2
        # sort from arr[lo:midpoint]
        mergesort(arr, lo, midpoint)
        # sort from arr[midpoint:hi]
        mergesort(arr, midpoint, hi)
        # merge
        merge(arr, lo, midpoint, hi)
    mergesort(arr, 0, len(arr))
    return arr

if __name__ == "__main__":
    test(sort)