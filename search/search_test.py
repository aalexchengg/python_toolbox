arr = [0,0,1,2,3,3,3,5,6,7,7,9,9,10,10]

def test_first(search):
    # print(search(arr, 1))
    assert(search(arr, 0) == 0)
    assert(search(arr, 1) == 2)
    assert(search(arr, 2) == 3)
    assert(search(arr, 3) == 4)
    assert(search(arr, 5) == 7)
    assert(search(arr, 7) == 9)
    assert(search(arr, 9) == 11)
    assert(search(arr,10) == 13)

    assert(search(arr, 4) == -1)
    print("All tests passed!")

def test_last(search):
    assert(search(arr, 0) == 1)
    assert(search(arr, 1) == 2)
    assert(search(arr, 2) == 3)
    assert(search(arr, 3) == 6)
    assert(search(arr, 5) == 7)
    assert(search(arr, 7) == 10)
    assert(search(arr, 9) == 12)
    assert(search(arr,10) == 14)
    
    assert(search(arr, 12) == -1)
    print("All tests passed!")
