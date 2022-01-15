L1 = []
L2 = []
base  = 2

n = base
f = 1
D = dict()

for i in range(15):
    n = n**0.5
    f /= 2
    L1.append(f)
    L2.append(n)
    D[f] = n

def show():
    for i,f in enumerate(L1):
        n = L2[i]
        print(str(f).ljust(18), f"{n:#.10g}")
        D[f] = n
    print('-'*10)

show()

#-----

import sys, math
target = float(sys.argv[1])
print(target)
print('-'*10)

value = 1
my_log = 0

for f in L1:
    n = D[f]
    tmp = n*value
    while tmp < target:
        my_log += f
        value = tmp
        print(value)
        tmp = n*value

print('-'*10)
print(my_log)
print(math.log(target,base))
    

