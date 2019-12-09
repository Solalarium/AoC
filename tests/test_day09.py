import sys
sys.path.insert(0, '.')
from util import Day
from day09 import *

def test_part1():
    part1 = Day(9,1)
    part1.load(typing=int,sep=',')
    part1.opcode(1)
    assert part1.result_list == [3335138414]

def test_part1_given0():
    part1 = Day(9,1)
    part1.load(data="109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99".split(','))
    part1.apply(int)
    part1.opcode()
    assert part1.result == 99

def test_part1_given1():
    part1 = Day(9,1)
    part1.load(data="1102,34915192,34915192,7,4,7,99,0".split(','))
    part1.apply(int)
    part1.opcode()
    assert part1.result == 1219070632396864

def test_part1_given2():
    part1 = Day(9,1)
    part1.load(data="104,1125899906842624,99".split(','))
    part1.apply(int)
    part1.opcode()
    assert part1.result == 1125899906842624