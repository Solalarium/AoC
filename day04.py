from util import Day

def is_pass_part1(x):
    x = str(x)
    if len(x) != 6: return False
    if x[0] <= x[1] <= x[2] <= x[3] <= x[4] <= x[5]:
        if x[0] == x[1] or x[1] == x[2] or x[2] == x[3] or x[3] == x[4] or x[4] == x[5]:
            return(True)
    return(False)

def is_pass_part2(x):
    x = str(x)
    if len(x) != 6: return False
    if x[0] <= x[1] <= x[2] <= x[3] <= x[4] <= x[5]:
        if x[0] == x[1] != x[2] or x[0] != x[1] == x[2] != x[3] or x[1] != x[2] == x[3] != x[4] or x[2] != x[3] == x[4] != x[5] or x[3] != x[4] == x[5]:
            return(True)
    return(False)

def counter(lower,upper,is_pass):
    count = 0
    for i in range(lower,upper+1):
        if is_pass(i): count += 1
    return(count)

if __name__ == '__main__':

    # --Part1-- result=1665
    day04 = Day(4,1)
    day04.load(int,sep='-')

    print(day04.answer(counter(day04.data[0],day04.data[1],is_pass_part1)))

    # --Part2-- result=1131
    day04 = Day(4,2)
    day04.load(int,sep='-')

    print(day04.answer(counter(day04.data[0],day04.data[1],is_pass_part2)))
