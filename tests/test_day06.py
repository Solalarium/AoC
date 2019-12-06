import sys
sys.path.insert(0, '.')
from util import Day
from day06 import *

def test_part1():
    part1 = Day(6,1)
    part1.load()

    orbit = make_orbit_dict(part1.data)

    nr_of_each_orbits = keyfinder(orbit,'COM',{},0)

    assert count_orbits(nr_of_each_orbits) == 139597

def test_part1_given0():
    part1 = Day(6,1)
    part1.load(data=['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L'])

    orbit = make_orbit_dict(part1.data)

    nr_of_each_orbits = keyfinder(orbit,'COM',{},0)

    assert count_orbits(nr_of_each_orbits) == 42

def test_part2():
    part2 = Day(6,2)
    part2.load()

    orbit = make_orbit_dict(part2.data)

    you = way_to_center(orbit,'YOU',[])
    san = way_to_center(orbit,'SAN',[])
    new_center = find_new_center(you,san)

    assert distance_to_center(orbit,new_center,'YOU')+distance_to_center(orbit,new_center,'SAN')-2 == 286

def test_part2_given0():
    part2 = Day(6,2)
    part2.load(data=['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN'])

    orbit = make_orbit_dict(part2.data)

    you = way_to_center(orbit,'YOU',[])
    san = way_to_center(orbit,'SAN',[])
    new_center = find_new_center(you,san)

    assert distance_to_center(orbit,new_center,'YOU')+distance_to_center(orbit,new_center,'SAN')-2 == 4
