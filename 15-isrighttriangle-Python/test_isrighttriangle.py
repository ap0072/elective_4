import pytest
from isrighttriangle import isrighttriangle
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('x1, y1, x2, y2, x3, y3, check', [
	(13, -1, -9, 3, -3, -9, False),
	(6, 1, 0, 4, -1, -7, False),
	(1, 2, 5, 4, -3, 0, False),
	(-1, 7, 10, -4, 12, -2, False),
	(5, 4, 11, 6, 15, -6, True)
])
def test_isrighttriangle(x1, y1, x2, y2, x3, y3, check):
    assert isrighttriangle(x1, y1,x2, y2,x3,y3) == check
