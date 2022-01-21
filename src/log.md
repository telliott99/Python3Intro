#### Logarithms

If we have a base `b` and a number `x`, then the logarithm of `x` to that base is `e` when

```
x = b^e
```

So if `x` is the square root of `b`, then the log of `x` is `0.5`.

To compute logarithms to a given base, we first establish successive square roots of that base.

```
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
```

which gives:

```
> p3 log2.py
0.5                1.414213562
0.25               1.189207115
0.125              1.090507733
0.0625             1.044273782
0.03125            1.021897149
0.015625           1.010889286
0.0078125          1.005429901
0.00390625         1.002711275
0.001953125        1.001354720
0.0009765625       1.000677131
0.00048828125      1.000338508
0.000244140625     1.000169240
0.0001220703125    1.000084616
6.103515625e-05    1.000042307
3.0517578125e-05   1.000021153
----------
```

Next, we use these stored values to compute the logarithm of an input value to base 2.  Here that value is 3.

```
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
```

```
> p3 /Users/telliott/Dropbox/Github/Python3Intro/log2.py 3
3.0
----------
1.4142135623730951
2.0000000000000004
2.8284271247461907
2.953652291878999
2.98581545658253
2.9939108235344714
2.9979667340823117
2.999996749374751
----------
1.5849609375
1.5849625007211563
> 
```

Proceeding down the list of exponents `(0.5, 0.25 ..)`, in the variable `f`, and the corresponding square roots `n`, we compute `tmp` as `n*value`.  

As long as `tmp` remains smaller than the target, we accumulate the exponent by adding them to the variable `my_log`, and assign `value = tmp`.  

In the output you can see `value` approaching but never exceeding the target.  At the end, the result is printed, together with the logarithm as computed by the built-in function.