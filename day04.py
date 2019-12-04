def split(x):
    if x >= 1000000 or x <= 99999: return(False)
    return([x//100000, (x % 100000)//10000, (x % 10000)//1000, (x % 1000)//100, (x % 100)//10, x % 10])

def is_pass_v1(x):
    if x == False: return(False)
    if x[0] <= x[1] <= x[2] <= x[3] <= x[4] <= x[5]:
        if x[0] == x[1] or x[1] == x[2] or x[2] == x[3] or x[3] == x[4] or x[4] == x[5]:
            return(True)
    return(False)

def is_pass(x):
    x = split(x)
    if x == False: return(False)
    if x[0] <= x[1] <= x[2] <= x[3] <= x[4] <= x[5]:
        if x[0] == x[1] != x[2] or x[0] != x[1] == x[2] != x[3] or x[1] != x[2] == x[3] != x[4] or x[2] != x[3] == x[4] != x[5] or x[3] != x[4] == x[5]:
            return(True)
    return(False)

def foo(lower,upper):
    count = 0
    for i in range(lower,upper+1):
        if is_pass(i): count += 1     
    return(count)      

#print(is_pass(split(223455)))
print(foo(158126,624574))
