from util import Day

def find_inputs(part2):
    for i in range(100):
        for j in range(100):
            part2.data[1] = i
            part2.data[2] = j
            if part2.opcode()[0] == 19690720:
                return(100 * i + j)
            part2.reset()

if __name__ == '__main__':

    # --Part01-- 3409710

    part1 = Day(2,1)
    part1.load(typing=int, sep=',')

    part1.data[1] = 12
    part1.data[2] = 2
    part1.opcode()
    print(part1.answer(part1.data[0]))

    # --Part02-- 7912

    part2 = Day(2,2)
    part2.load(typing=int, sep=',')

    print(part2.answer(find_inputs(part2)))