import sys
sys.path.insert(0, '.')
from util import Day
from day02 import *

def test_part01():
    part01 = Day(2,1)
    part01.load(typing=int, sep=',')
    
    part01.data[1] = 12
    part01.data[2] = 2
    assert compute(part01.data)[0] == 3409710