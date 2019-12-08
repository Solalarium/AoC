import sys
sys.path.insert(0, '.')
from util import Day
from day05 import *

def test_part1():
    part1 = Day(5,1)
    part1.load(typing=int,sep=',')
    part1.opcode(1)
    assert part1.result == 7692125

def test_part1_given_0():
    part1 = Day(5,1)
    part1.load(data="3,0,4,0,99".split(','))
    part1.apply(int)
    part1.opcode(1)
    assert part1.result == 1

def test_part2():
    part2 = Day(5,2)
    part2.load(typing=int,sep=',')
    part2.opcode(5)
    assert part2.result == 14340395

def test_part2_given_0():
    part2 = Day(5,2)
    part2.load(data="3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".split(','))
    part2.apply(int)
    part2.opcode(7)
    assert part2.result == 999
    part2.reset_apply()
    part2.opcode(8)
    assert part2.result == 1000
    part2.reset_apply()
    part2.opcode(9)
    assert part2.result == 1001