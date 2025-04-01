"""
Test suite goes here, as usual. You could improve this comment, while you're at it.
"""


from math import *    
from Logic import *

            
def segmentOverlap(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> bool:
    MODE: str = 'test samples'  # set to 'test samples' or 'mine'
    if Mode=='mine':
        return True  # REPLACE THIS WITH YOUR ALGORITHM
    elif MODE == 'test samples':
        from SegmentSamples import segmentOverlapSamples
# the line below only works in the QuaCS lab computers
#        from sample_answers.cs105.Intersect.SegmentSamples import segmentOverlapSamples
        answer: bool = circleOverlapSamples(x1, y1, r1, x2, y2, r2)
        return answer
    else:
        print('ERROR: You need to set MODE correctly in circleRectangleOverlap in circleRectangle.py')
        raise Exception


# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()
