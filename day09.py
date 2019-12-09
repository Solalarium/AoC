from util import Day

if __name__ == '__main__':
    # --Part 1-- input=1 result=3335138414
    part1 = Day(9,1)
    part1.load(typing=int, sep=',')
    part1.opcode(1)

    print(part1.answer())

    # --Part 2-- input=2 result=49122
    part2 = Day(9,2)
    part2.load(typing=int, sep=',')
    part2.opcode(2)

    print(part2.answer())