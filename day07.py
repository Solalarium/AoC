from util import Day

def find_max_sequence(amp_a, amp_b, amp_c, amp_d, amp_e, concurrent=False, x=range(5)):
    result = 0
    for a in x:
        for b in x:
            for c in x:
                for d in x:
                    for e in x:
                        if a not in [b,c,d,e] and b not in [c,d,e] and c not in [d,e] and d != e:
                            amp_a.reset_apply()
                            amp_b.reset_apply()
                            amp_c.reset_apply()
                            amp_d.reset_apply()
                            amp_e.reset_apply()
                            amp_a.concurrent = concurrent
                            amp_b.concurrent = concurrent
                            amp_c.concurrent = concurrent
                            amp_d.concurrent = concurrent
                            amp_e.concurrent = concurrent
                            amp_a.opcode_input = [a, 0]
                            amp_b.opcode_input = [b]
                            amp_c.opcode_input = [c]
                            amp_d.opcode_input = [d]
                            amp_e.opcode_input = [e]
                            temp = amping(a, amp_a, b, amp_b, c, amp_c, d, amp_d, e, amp_e)
                            if temp > result:
                                result = temp
                                maximum_sequenze = [a,b,c,d,e]
    return result,maximum_sequenze

def amping(a, amp_a, b, amp_b, c, amp_c, d, amp_d, e, amp_e):
    amp_a.opcode()
    amp_b.opcode_input.append(amp_a.result)
    amp_b.opcode()
    amp_c.opcode_input.append(amp_b.result)
    amp_c.opcode()
    amp_d.opcode_input.append(amp_c.result)
    amp_d.opcode()
    amp_e.opcode_input.append(amp_d.result)
    amp_e.opcode()
    amp_a.opcode_input.append(amp_e.result)
    if amp_e.concurrent is True:
        result = amping(a, amp_a, b, amp_b, c, amp_c, d, amp_d, e, amp_e)
    elif amp_e.concurrent is False:
        result = amp_e.result
    return result

def load_all(objs, data=None, concurrent=False):
    for obj in objs:
        obj.load(data=data, typing=int, sep=",")
        obj.apply(int)

if __name__ == '__main__':

    # --Part1-- 14902
    amp_a = Day(7, 1)
    amp_b = Day(7, 1)
    amp_c = Day(7, 1)
    amp_d = Day(7, 1)
    amp_e = Day(7, 1)
    obj = [amp_a, amp_b, amp_c, amp_d, amp_e]
    load_all(obj)
    result,_ = find_max_sequence(amp_a, amp_b, amp_c, amp_d, amp_e)
    print(amp_e.answer(result))

    # --Part2-- 6489132
    amp_a = Day(7, 2)
    amp_b = Day(7, 2)
    amp_c = Day(7, 2)
    amp_d = Day(7, 2)
    amp_e = Day(7, 2)
    obj = [amp_a, amp_b, amp_c, amp_d, amp_e]
    load_all(obj)
    result,_ = find_max_sequence(amp_a, amp_b, amp_c, amp_d, amp_e, concurrent=True, x=range(5,10))
    print(amp_e.answer(result))