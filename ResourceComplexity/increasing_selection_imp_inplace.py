"""
>>> myList = [4, 12, 3, 8]
>>> moveLowestToPosition(myList, 0)  # get lowest into position 0
>>> myList
[3, 12, 4, 8]
>>> moveLowestToPosition(myList, 1)  # put lowest after 1 into pos. 1
>>> myList  # this time, we find the 4, move it, save the 12 where it was
[3, 4, 12, 8]
"""

from Logic import *
from typing import List


def moveLowestToPosition(anyList: List[float], which: int) -> None:
    precondition(which >= 0 and which < len(anyList))
    smallestSoFar = anyList[which]
    whereSmallestWas = which
    for index in range(which, len(anyList)):
        if anyList[index] < smallestSoFar:   # bug fix ... had used index < smallestSoFar
            smallestSoFar = anyList[index]
            whereSmallestWas = index
    valueIAmGoingToOverwrite = anyList[which]
    anyList[which] = smallestSoFar
    anyList[whereSmallestWas] = valueIAmGoingToOverwrite





def makeIncreasing(anyList: List[float]) -> None:
    for putMeInPlace in range(len(anyList)):
        moveLowestToPosition(anyList, putMeInPlace)  # mutates anyList
    return # note the _list_object_ has been changed, without any "anyList = ..."


def increasing(anyList: List[float]) -> List[float]:
    copy = anyList + []  # look up "deepcopy" for a more general solution
    makeIncreasing(copy)
    return copy


if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")
