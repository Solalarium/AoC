import sys
sys.path.insert(0, '.')
from util import Day
from day07 import *

def test_part1_given0():
    part1 = Day(7,1)
    part1.load(data="3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(','))
    part1.apply(int)
    maximum,_ = find_max_sequence(part1)
    assert maximum == 43210

def test_part1_given1():
    part1 = Day(7,1)
    part1.load(data="3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0".split(','))
    part1.apply(int)
    maximum,_ = find_max_sequence(part1)
    assert maximum == 54321

def test_part1_given2():
    part1 = Day(7,1)
    part1.load(data="3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(','))
    part1.apply(int)
    maximum,_ = find_max_sequence(part1)
    assert maximum == 65210