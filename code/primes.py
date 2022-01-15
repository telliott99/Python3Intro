import sys
from math import sqrt

pL = [2,3]
t = int(sys.argv[1])

# having this as a function
# makes the break logic cleaner
def divisor_not_found(x):
    s = int(sqrt(x))
    for p in pL:
        #if p > s:
            #return True
        if x % p == 0:
            return False
    return True

def get_next_prime():
    tmp = pL[-1]
    tmp += 2
    while True:
        if divisor_not_found(tmp):
            break
        tmp += 2
    pL.append(tmp)
    
#------------------
        
def isPrime(n):
    while n > pL[-1]:
        get_next_prime()
    return n == pL[-1] or n in pL

def test(n):
    print(isPrime(n), pL)
    
test(t)
    
#------------------

def factors(n):
    rL = []
    for y in [2,3]:
        if n % y == 0:
            rL.append(y)
            n = n//y
        
    while n > 1:
        get_next_prime()
        top = pL[-1]
        while n % top == 0:
            n = n//top
            rL.append(top)
    return rL

print(factors(t))
        
'''
> p3 script.py 600851475143
[71, 839, 1471, 6857]
'''




