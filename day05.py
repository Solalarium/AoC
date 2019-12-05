from util import Day

# --Part01-- input=1 result=7692125
part1 = Day(5,1)
part1.load(int,',')

print(part1.answer(part1.opcode(1)))

# --Part02-- input=5 result=14340395
part2 = Day(5,2)
part2.load(int,',')

print(part2.answer(part2.opcode(5)))