from collections import defaultdict
from sort_tests import test

# stable, not in place, O(n)

def sort(arr):
    def isolate_digit(num: int, place: int):
        num = num // 10**place
        return num % 10
    def countingsort_radix(arr, place):
        # modified to be in place
        counter = defaultdict(lambda: list())
        for num in arr:
            counter[isolate_digit(num, place)].append(num)
        result = []
        for key in sorted(counter.keys()):
            for value in counter[key]:
                result.append(value)
        return result
    # LDS variant
    # get the maximum
    maximum = max(arr)
    # find number of places in the maximum
    max_places = 0
    while(maximum > 0):
        max_places += 1
        maximum = maximum // 10
    for i in range(max_places):
        arr = countingsort_radix(arr, i)
    return arr

if __name__ == "__main__":
    test(sort)

    
        



