from util import Day

day02 = Day(2,2)
day02.load(int,",")
data = day02.data

# memory[1] = 12
# memory[2] = 2

def op1(data,param1,param2,param3):
    data[param3] = data[param1] + data[param2]
    return data

def op2(data,param1,param2,param3):
    data[param3] = data[param1] * data[param2]
    return data

def opcode(memory,address):
    if   memory[address] == 1:
        memory = op1(memory,memory[address+1],memory[address+2],memory[address+3])
    elif memory[address] == 2:
        memory = op2(memory,memory[address+1],memory[address+2],memory[address+3])
    elif memory[address] == 99:
        return 0
    else:
        return None
    return memory

def compute(memory):
    instruction_pointer = 0
    while True:
        temp = opcode(memory,instruction_pointer)
        if temp == 0:
            break
        if temp == None:
            return None
        memory = temp
        instruction_pointer += 4
    return memory[0]

noun = 0
verb = 0

for noun in range(100):
    for verb in range(100):
        memory = data.copy()
        memory[1] = noun
        memory[2] = verb
        temp = compute(memory)
        if temp == 19690720:
            break
    if temp == 19690720:
        break

result = 100 * noun + verb
print(day02.answer(result))
# print(day02.answer(memory[0]))