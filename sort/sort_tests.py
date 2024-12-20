# Author: abcheng

from itertools import permutations
from random import sample
def test(sort_algorithm):
    assert(sort_algorithm([5,6,7,3,1,2,9,0]) == [0, 1,2,3,5,6,7,9])
    print("All tests passed!")
