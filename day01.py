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

day01 = Day(1,2)
day01.load(int)
day01.apply(fuelchain)

result = sum(day01.data)

print(day01.answer(result))