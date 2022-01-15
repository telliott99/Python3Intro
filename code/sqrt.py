import math

R = range(10)
def f(n):  return n**2

def search(L,t):
    # L is sorted
    # return the largest n with f(n) < t
    assert f(L[0]) < t
    for n in reversed(L):
        if f(n) <= t:
            return n
    # never reach here

def descend(n,level):
    e = eval('1e-' + str(level))
    L = [n + (e * x) for x in R]
    return search(L,2)

n = 1
for i in range(16):
    n = descend(n,i)
    print(str(n).rjust(18),str(n**2)[:i+3])

   
