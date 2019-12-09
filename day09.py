from util import Day

if __name__ == '__main__':
    # --Part01-- input=1 result=3335138414
    part1 = Day(9,1)
    part1.load(typing=int,sep=',')
    part1.opcode(1)

    print(part1.answer(part1.result_list))