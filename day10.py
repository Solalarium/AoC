from util import Day
from math import atan2,sqrt,sin,cos
from time import time

def find_max_asteroid(obj):
    max_result = 0
    max_y = 0
    max_x = 0
    for y in range(0,len(obj.data)):
        for x in range(0,len(obj.data[y])):
            if obj.data[y][x] == '#':
                result = how_many_in_line_of_sight(obj,y,x)
                if result > max_result:
                    max_result = result
                    max_y = y
                    max_x = x
    return max_result, max_x, max_y

def how_many_in_line_of_sight(obj,y1,x1):
    counter = 0
    for y2 in range(0,len(obj.data)):
        for x2 in range(0,len(obj.data[y2])):
            if obj.data[y2][x2] == '#':
                if can_be_seen(obj,y1,x1,y2,x2) == True:
                    counter += 1
    return counter

def can_be_seen(obj,y1,x1,y2,x2):
    if y1 == y2 and x1 == x2:
        return False
    elif y1 == y2 and x1 != x2:
        if x1 < x2:
            for px in range(x1+1,x2):
                if obj.data[y1][px] == '#':
                    return False
        else:
            for px in range(x2+1,x1):
                if obj.data[y1][px] == '#':
                    return False
    elif y1 != y2 and x1 == x2:
        if y1 < y2:
            for py in range(y1+1,y2):
                if obj.data[py][x1] == '#':
                    return False
        else:
            for py in range(y2+1,y1):
                if obj.data[py][x1] == '#':
                    return False
    elif y1 < y2 and x1 < x2:
        for py in range(y1+1,y2):
            for px in range(x1+1,x2):
                if (py-y1)/(y2-y1) == (px-x1)/(x2-x1):
                    if obj.data[py][px] == '#':
                        return False
    elif y1 > y2 and x1 < x2:
        for py in range(y2+1,y1):
            for px in range(x1+1,x2):
                if (py-y1)/(y2-y1) == (px-x1)/(x2-x1):
                    if obj.data[py][px] == '#':
                        return False
    elif y1 < y2 and x1 > x2:
        for py in range(y1+1,y2):
            for px in range(x2+1,x1):
                if (py-y1)/(y2-y1) == (px-x1)/(x2-x1):
                    if obj.data[py][px] == '#':
                        return False
    elif y1 > y2 and x1 > x2:
        for py in range(y2+1,y1):
            for px in range(x2+1,x1):
                if (py-y1)/(y2-y1) == (px-x1)/(x2-x1):
                    if obj.data[py][px] == '#':
                        return False
    return True

def kart_to_polar(obj):
    _,x1,y1 = find_max_asteroid(obj)
    koord_dict = {}
    for y in range(0,len(obj.data)):
        for x in range(0,len(obj.data[y])):
            if obj.data[y][x] == '#':
                if can_be_seen(obj,y1,x1,y,x):
                    koord_dict[(y,x)] = (atan2(y,x),sqrt(x**2+y**2))
    return koord_dict

def vaporize(obj,counter,end=200):
    koord_dict = kart_to_polar(obj)
    for k in koord_dict.keys():
        y,x = koord_dict[k]
        obj.data[y][x] = '.'
        counter += 1
        if counter == end:
            return x,y
        elif counter < end:
            return vaporize(obj,counter,end)


# def 
if __name__ == '__main__':
    # bla = time()
    # part1 = Day(10,1)
    # part1.load()
    # part1.apply(list)

    # print(find_max_asteroid(part1))
    # print(time()-bla)

    part2 = Day(10,2)
    part2.load(data=""".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".split())
part2.apply(list)

print(vaporize(part2,0))

                