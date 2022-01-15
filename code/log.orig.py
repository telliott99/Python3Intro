''' 
this script computes the logarithm of the first arg
to the base given in the second arg
the first output is the result
the second output is from the built-in log function
'''

from functools import reduce
import math
import sys

try:
    n = float(sys.argv[1])
    base = float(sys.argv[2])
    
except IndexError:
    print('usage: python3 log.py number base')
    sys.exit()
# -------
L = [base]
rL = []

# dict from root to logarithm
# for roots:  1, 0.5, 0.25, 0.125 etc.
D = {}

# 5 place accuracy
b = L[-1]
i = 1
D[b] = i

while b > 1.00001:
    b = b**0.5
    i /= 2
    D[b] = i
    L.append(b)

if 'D' in sys.argv: 
    for b in L:
        print(b,D[b])
    sys.exit()
# -------
t = 1

for factor in L:
    while True:
        tmp = t * factor
        if tmp < n:
            t = tmp
            # print(t,factor)
            rL.append(D[factor])
        else:
            break

print(sum(rL))
print(math.log(n,base))

'''
> p3 log.py 10 2 D
2.0 1
1.4142135623730951 0.5
1.189207115002721 0.25
1.0905077326652577 0.125
1.0442737824274138 0.0625
1.0218971486541166 0.03125
1.0108892860517005 0.015625
1.0054299011128027 0.0078125
1.0027112750502025 0.00390625
1.0013547198921082 0.001953125
1.0006771306930664 0.0009765625
1.0003385080526823 0.00048828125
1.0001692397053021 0.000244140625
1.0000846162726942 0.0001220703125
1.0000423072413958 6.103515625e-05
1.0000211533969647 3.0517578125e-05
1.0000105766425498 1.52587890625e-05
1.0000052883072919 7.62939453125e-06
>
> p3 log.py 2 2.718281828
0.693147180676533
0.6931471806769994
> p3 log.py 2 2.718281828
0.693147180676533
0.6931471806769994
> p3 log.py 10 100       
0.5
0.5
> p3 log.py 1 2          
0
0.0
> p3 log.py 10 3         
2.095903274288503
2.095903274289385
> 
'''
     