from util import Day

def find_max_sequence(part1):
    result = 0
    x = range(5)
    for a in x:
        for b in x:
            for c in x:
                for d in x:
                    for e in x:
                        if a not in [b,c,d,e] and b not in [c,d,e] and c not in [d,e] and d != e:
                            part1.result = 0
                            part1.reset_apply()
                            part1.opcode(input1=a)
                            part1.opcode_input = part1.result
                            part1.reset_apply()
                            part1.opcode(input1=b)
                            part1.opcode_input = part1.result
                            part1.reset_apply()
                            part1.opcode(input1=c)
                            part1.opcode_input = part1.result
                            part1.reset_apply()
                            part1.opcode(input1=d)
                            part1.opcode_input = part1.result
                            part1.reset_apply()
                            part1.opcode(input1=e)
                            if part1.result > result:
                                result = part1.result
                                maximum_sequenze = [a,b,c,d,e]
    return result,maximum_sequenze

if __name__ == '__main__':

    # --Part1--
    part1 = Day(7,1)
    part1.load(typing=int, sep=',')
    print(find_max_sequence(part1))

    # --Part2--
    part2 = Day(7,2)
    part2.load(typing=int, sep=',')
    print(find_max_sequence(part2))