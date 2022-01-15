#### Newton-Raphson

This method takes an approximate initial value for  &radic; N, call it `x`, and produces a better guess `g`.

We use `x` to obtain something which is "on the other side" of the target:  `N/x` and then average the two values:

```
g = (x + N/x)/2
```

This works if `x` is not zero.  

#### Justification

The line through the point (x,f(x)) with slope f'(x) goes through y = 0 when x = g, because the slope is 

f'(x) = &Delta;y/&Delta;x = [f(x) - 0] / [x - g]

g = x - f(x)/f'(x)

To evaluate this, we write an expression f(x) (where the values we seek are the roots f(x) = 0)

f(x) = x^2 - N

f'(x) = 2x

The ratio is 

f(x)/f'(x) = x/2 - N/(2x) = (x - N/x)/2

Substituting, we obtain

g = (x + N/x)/2

(more discussion [here](../pdf/Newton.pdf)
 
#### Python

```
>>> def improve(x,N):
...     return (x + N/x)/2
... 
>>> g = 2
>>> for i in range(4):
...     g = improve(g,2)
...     print(g, g*g)
... 
1.5 2.25
1.4166666666666665 2.006944444444444
1.4142156862745097 2.0000060073048824
1.4142135623746899 2.0000000000045106
1.414213562373095 1.9999999999999996
>>>
```

Here's a more sophisticated version:

**script.py**

```
import sys
N = int(sys.argv[1])

def make():
    return lambda x: (x + N/x)/2

improve = make()
g = 2

while abs(g*g - N) > 1e-9:
    print(g)
    g = improve(g)

print(g)
```

which outputs:

```
> p3 script.py 2
2
1.5
1.4166666666666665
1.4142156862745097
1.4142135623746899
> p3 script.py 3
2
1.75
1.7321428571428572
1.7320508100147274
1.7320508075688772
> p3 script.py 5
2
2.25
2.236111111111111
2.2360679779158037
2.23606797749979
>
```

Notes:  in

```
def make():
    return lambda x: (x + N/x)/2
```

we are returning a function that is specialized for the particular value of `N`.  We could give that function a name like `f`

```
def make():
    def f(x):
        return (x + N/x)/2
        
    return f
```

The lambda construct is an "anonymous" function.  The `f` is a name that we never use again, so why bother with it?

Another point is

```
while abs(g*g - N) > 1e-9:
```

Since we use `g = 2` for each `N`, `g*g - N` is not positive for `N >= 2`, so the while loop never executes without `abs`, which calls the absolute value function.  Without `abs` the code works find for N = 2 or 3 but not for N = 5.
