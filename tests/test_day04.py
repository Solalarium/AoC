import sys
sys.path.insert(0, '.')
from util import Day
from day04 import *

def test_original():
    day04 = Day(4,1)
    day04.load(int,sep='-')

    assert counter(day04.data[0],day04.data[1],is_pass_part1) == 1665
    assert counter(day04.data[0],day04.data[1],is_pass_part2) == 1131

def test_part1_given():
    assert is_pass_part1(111111)
    assert is_pass_part1(223450) == False
    assert is_pass_part1(123789) == False
    assert is_pass_part1(11234) == False

def test_part2_given():
    assert is_pass_part2(112233)
    assert is_pass_part2(123444) == False
    assert is_pass_part2(111122)
    assert is_pass_part2(11234) == False