from util import Day

def fuel(data):
    return(data//3-2)

def fuelchain(data):
    fuel = data
    data = 0
    while fuel>0:
        fuel = fuel//3-2
        if fuel>0:
            data += fuel
    return(data)

if __name__ == '__main__':

    # --Part 1-- 3295206
    part1 = Day(1,1)
    part1.load(int)
    part1.apply(fuel)

    result = sum(part1.data)

    print(part1.answer(result))

    # --Part 2-- 4939939
    part2 = Day(1,2)
    part2.load(int)
    part2.apply(fuelchain)

    result = sum(part2.data)

    print(part2.answer(result))