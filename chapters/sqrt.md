#### Calculating the square root of 2

[script.py](../code/sqrt.py)

```
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
    print(str(n).rjust(18),n**2)
```


```
> p3 script.py
               1.0 1.0
               1.4 1.9599999999999997
              1.41 1.9880999999999998
             1.414 1.9993959999999997
            1.4142 1.9999616399999998
           1.41421 1.9999899240999999
          1.414213 1.9999984093689998
         1.4142135 1.99999982358225
        1.41421356 1.9999999932878738
       1.414213562 1.999999998944728
      1.4142135623 1.999999999793256
     1.41421356237 1.9999999999912461
    1.414213562373 1.9999999999997315
    1.414213562373 1.9999999999997315
  1.41421356237309 1.9999999999999858
 1.414213562373094 1.9999999999999971
>
``` 