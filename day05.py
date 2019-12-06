from util import Day

# --Part01-- input=1 result=7692125
part1 = Day(5,1)
part1.load(typing=int,sep=',')
part1.opcode(1)

print(part1.answer(part1.result))

# --Part02-- input=5 result=14340395
part2 = Day(5,2)
part2.load(typing=int,sep=',')
part2.opcode(5)

print(part2.answer(part2.result))