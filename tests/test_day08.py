import sys
sys.path.insert(0, '.')
from util import Day
from day08 import *

def test_part1():
    part1 = Day(8,1)
    part1.load(typing=str)
    layers = get_layers(part1, 25, 6)
    zero_layer = fewest_zero_layer(layers)
    assert number_of_x_digits(layers,zero_layer,'1')*number_of_x_digits(layers,zero_layer,'2') == 1088