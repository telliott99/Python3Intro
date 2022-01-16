# representing binary numbers as strings of 0 and 1
import sys

def help():
    hL = ['please input two binary numbers, for example:',
         'p3 binops.py 00110 1111001',
         'default is addition, for multiplication add -m flag']
    return('\n'.join(hL))

args = sys.argv
args.pop(0)

m = '-m' in args
if m:  args.remove('-m')

try:
    x,y = args[:2]
except ValueError:
    print(help)
    sys.exit()

#--------------------------

# format with additional leading zeros
# so x and y are the same length

def extend(b,n):
    return ('0'*n) + b
    
def pad(x,y):
    delta = len(x) - len(y)
    if delta > 0:
        y = extend(y,delta)
    elif delta < 0:
        x = extend(x,-delta)
    return x,y

#--------------------------

def addn(x,y):
    rL = []
    carry = 0
    # reverse both strings
    for a,b in zip(x[::-1],y[::-1]):
    
        # central part of the logic
        value = int(a) + int(b) + carry
        if value in [2,3]:
            carry = 1
        else:
            carry = 0
        if value in [1,3]:
            rL.append('1')
        else:
            rL.append('0')
            
    if carry == 1:
        rL.append('1')
    return ''.join(reversed(rL))
    
def add_all(L):
    # adjust lengths first
    n = max([len(b) for b in L])
    L = [extend(b,n-len(b)) for b in L]
    result = L.pop()
    while L:
        y = L.pop()
        result = addn(result,y)
    return result

def multiply(x,y):
    mL = list()
    for i,digit in enumerate(y[::-1]):
        if digit == '1':
            mL.append(x + '0'*i)
    return mL, add_all(mL)
    
#--------------------------

def show(L):
    n = max([len(w) for w in L])
    for w in L:
        print(w.rjust(n))
    print()

x,y = pad(x,y)

if m:
    mL, result = multiply(x,y)
    line = '-' * len(result)
    show([x,y,line] + mL + [line,result])
else:
    result = addn(x,y)
    line = '-' * len(result)
    show([x,y,line,result])
    
'''
> p3 binops.py 00110 1111011   
 0000110
 1111011
--------
10000001

> p3 binops.py -m 101 11    
 101
 011
----
 101
1010
----
1111

> p3 binops.py -m 00110 1111011
      0000110
      1111011
-------------
      0000110
     00001100
   0000110000
  00001100000
 000011000000
0000110000000
-------------
0001011100010

> 
'''