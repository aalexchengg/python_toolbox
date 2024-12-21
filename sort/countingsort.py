# author: abcheng
from sort_tests import test

# stable, not in place, O(n)

def sort(arr):
    maximum = max(arr)
    counter = [0 for _ in range(maximum + 1)]
    for num in arr:
        counter[num] += 1
    i = 0
    for num, count in enumerate(counter):
        for j in range(count):
            arr[i] = num
            i += 1
    assert(i == len(arr))
    return arr


if __name__ == "__main__":
    test(sort)
