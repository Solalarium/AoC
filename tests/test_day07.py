import sys
sys.path.insert(0, '.')
from util import Day
from day07 import *

def test_part1():
    amp_a = Day(7, 1)
    amp_b = Day(7, 1)
    amp_c = Day(7, 1)
    amp_d = Day(7, 1)
    amp_e = Day(7, 1)
    obj = [amp_a, amp_b, amp_c, amp_d, amp_e]
    load_all(obj)
    maximum,_ = find_max_sequence(amp_a, amp_b, amp_c, amp_d, amp_e)
    assert maximum == 14902

def test_part1_given0():
    amp_a = Day(7, 1)
    amp_b = Day(7, 1)
    amp_c = Day(7, 1)
    amp_d = Day(7, 1)
    amp_e = Day(7, 1)
    obj = [amp_a, amp_b, amp_c, amp_d, amp_e]
    load_all(obj, data="3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(','))
    maximum,_ = find_max_sequence(amp_a, amp_b, amp_c, amp_d, amp_e)
    assert maximum == 43210

def test_part1_given1():
    amp_a = Day(7, 1)
    amp_b = Day(7, 1)
    amp_c = Day(7, 1)
    amp_d = Day(7, 1)
    amp_e = Day(7, 1)
    obj = [amp_a, amp_b, amp_c, amp_d, amp_e]
    load_all(obj, data="3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0".split(','))
    maximum,_ = find_max_sequence(amp_a, amp_b, amp_c, amp_d, amp_e)
    assert maximum == 54321

def test_part1_given2():
    amp_a = Day(7, 1)
    amp_b = Day(7, 1)
    amp_c = Day(7, 1)
    amp_d = Day(7, 1)
    amp_e = Day(7, 1)
    obj = [amp_a, amp_b, amp_c, amp_d, amp_e]
    load_all(obj, data="3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(','))
    maximum,_ = find_max_sequence(amp_a, amp_b, amp_c, amp_d, amp_e)
    assert maximum == 65210

def test_part2():
    amp_a = Day(7, 2)
    amp_b = Day(7, 2)
    amp_c = Day(7, 2)
    amp_d = Day(7, 2)
    amp_e = Day(7, 2)
    obj = [amp_a, amp_b, amp_c, amp_d, amp_e]
    load_all(obj)
    maximum,_ = find_max_sequence(amp_a, amp_b, amp_c, amp_d, amp_e, concurrent=True, x=range(5,10))
    assert maximum == 6489132

def test_part2_given0():
    amp_a = Day(7, 2)
    amp_b = Day(7, 2)
    amp_c = Day(7, 2)
    amp_d = Day(7, 2)
    amp_e = Day(7, 2)
    obj = [amp_a, amp_b, amp_c, amp_d, amp_e]
    load_all(obj, data="3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(','))
    maximum,_ = find_max_sequence(amp_a, amp_b, amp_c, amp_d, amp_e, concurrent=True, x=range(5,10))
    assert maximum == 139629729

def test_part2_given1():
    amp_a = Day(7, 2)
    amp_b = Day(7, 2)
    amp_c = Day(7, 2)
    amp_d = Day(7, 2)
    amp_e = Day(7, 2)
    obj = [amp_a, amp_b, amp_c, amp_d, amp_e]
    load_all(obj, data="3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10".split(','))
    maximum,_ = find_max_sequence(amp_a, amp_b, amp_c, amp_d, amp_e, concurrent=True, x=range(5,10))
    assert maximum == 18216