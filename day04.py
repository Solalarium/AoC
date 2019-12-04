def split(x):
    return([x//100000, (x % 100000)//10000, (x % 10000)//1000, (x % 1000)//100, (x % 100)//10, x % 10])

def ispass(x):
    if x[0] <= x[1] <= x[2] <= x[3] <= x[4] <= x[5]:
        if x[0] == x[1] or x[1] == x[2] or x[2] == x[3] or x[3] == x[4] or x[4] == x[5]:
            return(True)
    return(False)

def bla(lower,upper):    
    count = 0
    for i in range(lower,upper+1):
        if ispass(split(i)):
            count += 1
    return(count)      


print(bla(158126,624574))
#print(ispass(testdata))