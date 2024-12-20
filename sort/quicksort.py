from random import randint
from sort_tests import test

def sort(arr: list):
    
    def swap(arr, i ,j):
        arr[i], arr[j] = arr[j], arr[i]
    
    def partition(arr, lo, hi):
        # lo and hi are INCLUSIVE.
        # if the array is of length 1 or 0, return
        if hi - lo < 1 :
            return lo
        # select a random pivot (note: most algorithms just use the hi for ease, but i made it random in the spirit of the algorithm)
        pivot = randint(lo, hi)
        # and then move it to the end
        swap(arr, pivot, hi)
        # create a pointer to the bottom and top of the unsorted area
        i = lo
        j = hi - 1
        while (i != j):
            if arr[i] < arr[hi]:
                i += 1
            else:
                swap(arr, i , j)
                j -= 1
        # at this point, i is either the first integer greater than pivot, or the one before it
        # if its the one before it, increment by one.
        if (arr[i] < arr[hi]):
            i += 1 
        # swap it and put it in the right place
        swap(arr, i, hi)
        return i
    
    def quicksort(arr, lo, hi):
        # lo and hi are inclusive
        if (hi - lo) < 1:
            return 
        # partition between left and right of pivot
        p = partition(arr, lo, hi)
        # dont include the pivot when running quicksort recursively
        quicksort(arr, lo, p-1)
        quicksort(arr, p+1, hi)
    quicksort(arr, 0, len(arr) - 1)
    return arr

if __name__ == "__main__":
    test(sort)





        