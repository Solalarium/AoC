import numpy as np
from util import Day

# 159       610
# data = np.array([["R75","D30","R83","U83","L12","D49","R71","U7","L72"],["U62","R66","U55","R34","D71","R55","D58","R83"]])

# 135       410
# data = np.array([["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]])

# 6         30
# data = np.array([["R8","U5","L5","D3"],["U7","R6","D4","L4"]])
def splitter(day03):
    data = np.array([day03.data[0].split(','),day03.data[1].split(',')])
    val = np.array([np.array(np.char.lstrip(data[0], 'LRUD'), dtype=int), np.array(np.char.lstrip(data[1], 'LRUD'), dtype=int)])
    direction = np.array([np.char.rstrip(data[0], '0123456789'), np.char.rstrip(data[1], '0123456789')])
    return val,direction

def mapsize(val,direction):
    i = 0
    x = 0
    y = 0
    xmin = 0
    ymin = 0
    xmax = 0
    ymax = 0
    while i < val.size:
        if   direction[i] == 'L':
            x -= val[i]
            if x < xmin:
                xmin = x
        elif direction[i] == 'R':
            x += val[i]
            if x > xmax:
                xmax = x
        elif direction[i] == 'U':
            y -= val[i]
            if y < ymin:
                ymin = y
        elif direction[i] == 'D':
            y += val[i]
            if y > ymax:
                ymax = y
        else:
            return None
        # print(ymax,ymin,xmax,xmin)
        i += 1
    # print("mapsize check",y,x,cy,cx)
    return ymax,ymin,xmax,xmin

def init_map(val,direction):
    size1 = mapsize(val[0], direction[0])
    size2 = mapsize(val[1], direction[1])

    ymax  = 0
    ymin  = 0
    xmax = 0
    xmin = 0

    if size1[0] > size2[0]:
        ymax  = size1[0]
    else:
        ymax  = size2[0]
    if size1[1] < size2[1]:
        ymin  = size1[1]
    else:
        ymin  = size2[1]
    if size1[2] > size2[2]:
        xmax  = size1[2]
    else:
        xmax  = size2[2]
    if size1[3] < size2[3]:
        xmin  = size1[3]
    else:
        xmin  = size2[3]

    x  = xmax-xmin+1
    y  = ymax-ymin+1
    cx = abs(xmin)
    cy = abs(ymin)

    kablemap = np.zeros((y,x), dtype=int)

    return kablemap,cx,cy

def draw(kablemap,val,direction,cy,cx):
    j = 0
    while j < val.shape[0]:
        i = 0
        kable = j+1
        y = cy
        x = cx
        kablemap[y][x] = 8
        while i < val[j].size:
            if   direction[j][i] == 'L':
                tempx = x
                while tempx > x-val[j][i]:
                    tempx -= 1
                    if kablemap[y][tempx] == 0:
                        kablemap[y][tempx] = kable
                    elif kablemap[y][tempx] != kable:
                        kablemap[y][tempx] = 3
                x = tempx
            elif direction[j][i] == 'R':
                tempx = x
                while tempx < x+val[j][i]:
                    tempx += 1
                    if kablemap[y][tempx] == 0:
                        kablemap[y][tempx] = kable
                    elif kablemap[y][tempx] != kable:
                        kablemap[y][tempx] = 3
                x = tempx
            elif direction[j][i] == 'U':
                tempy = y
                while tempy > y-val[j][i]:
                    tempy -= 1
                    if kablemap[tempy][x] == 0:
                        kablemap[tempy][x] = kable
                    elif kablemap[tempy][x] != kable:
                        kablemap[tempy][x] = 3
                y = tempy
            elif direction[j][i] == 'D':
                tempy = y
                while tempy < y+val[j][i]:
                    tempy += 1
                    if kablemap[tempy][x] == 0:
                        kablemap[tempy][x] = kable
                    elif kablemap[tempy][x] != kable:
                        kablemap[tempy][x] = 3
                y = tempy
            else:
                return None
            i += 1
        j += 1
    # print("draw check")
    return kablemap

def distance(kablemap,cy,cx):
    return min(abs(x[0]-cy) + abs(x[1]-cx)  for x in np.argwhere(kablemap==3))

def minway(kablemap,val,direction,cy,cx):
    minsteps = np.inf
    for z in np.argwhere(kablemap==3):    
        j = 0
        steps = 0
        # print(z[0],z[1])
        while j < val.shape[0]:
            i = 0
            y = cy
            x = cx
            cont = True
            # print(j)
            while i < val[j].size and cont:
                for _ in range(val[j][i]):
                    if   direction[j][i] == 'L':
                        x -= 1
                    elif direction[j][i] == 'R':
                        x += 1
                    elif direction[j][i] == 'U':
                        y -= 1
                    elif direction[j][i] == 'D':
                        y += 1
                    else:
                        return None
                    steps += 1
                    if z[0] == y and z[1] == x:
                        cont = False
                        break
                i += 1
            j += 1
        # print(steps)
        if steps < minsteps:
            minsteps = steps
    return minsteps

if __name__ == '__main__':

    day03 = Day(3,1)
    day03.load()

    val,direction = splitter(day03)
    kablemap,cx,cy = init_map(val,direction)
    kablemap = draw(kablemap, val, direction, cy, cx)

    # --Part1-- result=1285
    print(distance(kablemap, cy, cx))

    # --Part2-- result=14228
    print(minway(kablemap, val, direction, cy, cx))

