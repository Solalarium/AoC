import sys
sys.path.insert(0, '.')
from util import Day
from day03 import *


def test_original():
    day03 = Day(3,1)
    day03.load()

    val,direction = splitter(day03)
    kablemap,cx,cy = init_map(val,direction)
    kablemap = draw(kablemap, val, direction, cy, cx)

    assert distance(kablemap, cy, cx) == 1285
    assert minway(kablemap, val, direction, cy, cx) == 14228

def test_given_0():
    day03 = Day(3,1)
    day03.load(data="""R8,U5,L5,D3\nU7,R6,D4,L4""".split())

    val,direction = splitter(day03)
    kablemap,cx,cy = init_map(val,direction)
    kablemap = draw(kablemap, val, direction, cy, cx)

    assert distance(kablemap, cy, cx) == 6
    assert minway(kablemap, val, direction, cy, cx) == 30

def test_given_1():
    day03 = Day(3,1)
    day03.load(data="""R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83""".split())

    val,direction = splitter(day03)
    kablemap,cx,cy = init_map(val,direction)
    kablemap = draw(kablemap, val, direction, cy, cx)

    assert distance(kablemap, cy, cx) == 159
    assert minway(kablemap, val, direction, cy, cx) == 610

def test_given_2():
    day03 = Day(3,1)
    day03.load(data="""R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7""".split())

    val,direction = splitter(day03)
    kablemap,cx,cy = init_map(val,direction)
    kablemap = draw(kablemap, val, direction, cy, cx)

    assert distance(kablemap, cy, cx) == 135
    assert minway(kablemap, val, direction, cy, cx) == 410
