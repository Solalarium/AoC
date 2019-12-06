import sys
sys.path.insert(0, '.')
from util import Day
from day02 import *

def test_part1():
    part1 = Day(2,1)
    part1.load(typing=int, sep=',')
    
    part1.data[1] = 12
    part1.data[2] = 2
    part1.opcode()
    assert part1.data[0] == 3409710

def test_part2():
    part2 = Day(2,1)
    part2.load(typing=int, sep=',')
    assert find_inputs(part2) == 7912