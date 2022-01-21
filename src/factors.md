As part of our introduction to programming, we'll look at some problems involving integers.  The first is

#### Fibonacci numbers

As I'm sure you know, the Fibonacci numbers are defined by the recurrence relation:

```
Fn = F{n-1} + F{n-2}
```

The first two elements are usually defined to be `[1,1]`.

```
a = 1
b = 1 
for i in range(5):
    tmp = a + b
    b = a
    a = tmp
    print(b,a)
```

We used a temporary value (`tmp`) here, because the new value of `a` refers to the old `b`, but the new value of `b` refers to the old `a`.  It's a chicken-and-egg problem.

There are other possible solutions.  We can use a list.

```
L = [1,1]
for i in range(10):
    next = L[-2] + L[-1]
    L.append(next)

print(L)
```

```
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
```

Or even more pithily:

```
>>> n = 10
>>> L = [1,1]
>>> for i in range(n):
...     L.append(L[-1] + L[-2])
... 
>>> L
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
>>>
```

We might also use a tuple assignment.  Tuple assignment caches the old values:

```
>>> a,b = 1,1
>>> a,b = a+b,a
>>> a,b
(2, 1)
>>>
```

so

```
>>> a,b = 1,1
>>> for i in range(10):
...     print(a)
...     a,b = a+b,a
... 
1
2
3
5
8
13
21
34
55
89
>>>
```

#### Factoring

As an example of how programs are developed in stages (at least, that's how I do it), we will write a program to find the prime factors for an integer.

We start simply, with integers smaller than 25, so we need to test only the first two prime numbers.

```
L = [2,3]
n = 6
for p in L:
    if n % p == 0:
        print(p)
```

```
> p3 factors.py
2
3
> 
```

That seems to work OK.

How to easily try different numbers?  Bring them in on the command line:

```
import sys
n = int(sys.argv[1])

L = [2,3]
for p in L:
    if n % p == 0:
        print(p)
```

```
> p3 factors.py 6 
2
3
> p3 factors.py 10
2
> 
```

Do you see what happened?  We found one prime factor of 10 but not the other one.

```
import sys
n = int(sys.argv[1])

L = [2,3]
for p in L:
    if n % p == 0:
        print(p)
        n = n // p
print(n)
```

```
> p3 factors.py 10
2
5
>
```

We use integer division `//`.

In Python3, unlike Python 2, the division operator `/` converts its arguments to floats and returns a float result


```
> p3 factors.py 2 
2
1
>
```

I don't like that `1`.  It's not a prime number.  But, that's easy to fix.

```
import sys
n = int(sys.argv[1])

L = [2,3]
for p in L:
    if n % p == 0:
        print(p)
        n = n // p
if n != 1:
    print(n)
```

```
> p3 factors.py 2
2
>
```

We also need to deal with the case where a prime factor is repeated.  Can you spot the change to the code below and explain why it works?

```
pL = [2,3,5,7]

def factors(n):
    rL = []
    for p in pL:
        while n % p == 0:
            rL.append(p)
            n = n // p
    if n > 1:
        rL.append(n)
    return rL

for n in range(2,101):
    L = factors(n)
    print(n,L)
```

``` 
> p3 factors.py  
2 [2]
3 [3]
4 [2, 2]
5 [5]
...
97 [97]
98 [2, 7, 7]
99 [3, 3, 11]
100 [2, 2, 5, 5]
>
```
