Let's do some more computing with numbers, say, the prime numbers.

#### Primes

The easiest way to get prime numbers is to load them from a file.  Lists of primes are available on the internet (e.g. [here](https://primes.utm.edu/lists/) ).

I have edited the file so it contains only primes and not the header and footer originally present, making it easier to load the data.

```
>>> with open('data/primes.txt') as fh:
...     data = fh.read()
>>> L = [int(n) for n in data.strip().split()]
>>> L[:5]
[2, 3, 5, 7, 11]
>>>
```

The only trick is that the numbers come into our program as strings.  To do math with them, they must be converted to integer form.

#### Checking for primality

As practice in programming, let's look at some programs to generate the prime numbers.  We start simply and improve as we go.

Here is a function that checks whether `n` is prime:

```
def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
```

`isPrime` tests *every* `i` in the list `[2, 3, n-1]` for whether `i` divides `n` evenly.

We might exercise it like so:

```
pL = [n for n in range(2,20) if isPrime(n)]
print(pL)
```

```
> p3 primes.py
[2, 3, 5, 7, 11, 13, 17, 19]
```

The code uses a list comprehension to construct a list that holds the resulting primes.

```
pL = [n for n in range(2,30) if isPrime(n)]
```

`isPrime` works when `n` is equal to `2`.

But it does so only because `range(2,2)` does not contain any elements, so the loop is skipped and the function returns `True`.

A first improvement is to only check odd numbers for whether they are prime, since no even number other than `2` is prime.  

We can do this by adjusting the `range`.

```
def isPrime(n):
    for i in range(3,n,2):
        if n % i == 0:
            return False
    return True
```

With this approach, the special case of `n` equal `2` actually returns the correct result, again, somewhat by accident, but it fails for even numbers, since we never tested for multiples of `2`.

```
def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3,n,2):
        if n % i == 0:
            return False
    return True
```

This code works, but it still has a problem, it's wasteful.  We should only check candidates until `i` exceeds the square root of `n` (or `i*i > n`, which amounts to the same thing).

```
def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3,n,2):
        if n % i == 0:
            return False
        if i * i > n:
            return True
    return True
```

Another thing is that we compute `i*i` repeatedly, for each `n` that is checked.  It would be much better to cache the result.  A dictionary works well.  For example

```
D = dict()
```

and then after checking if `n % i == 0` do this:

```
        if i in D:
            sq = D[i]
        else:
            sq = i*i
            D[i] = sq
        if sq > n:
		     return True
```

The line `if i in D` checks whether `i` is one of the *keys* in the dictionary.  If it is, we get the corresponding value with `D[i]`, otherwise we construct the value and save it for later.

#### More

Suppose we know all the primes up to a certain number and they are contained in a list of primes, like

```
L = [2, 3, 5]
```

The next prime `p` has the properties that `p > 5` but also

- `p` has no factors other than itself and 1

Now, any integer has a unique prime factorization (this is called the fundamental theorem of arithmetic).

If `p` has no prime factors, then it has no factors of any kind, other than itself and 1.  (If it did, then it would have prime factors, since those factors would have their own prime factorizations).

As a result, to find the next `p`, we need only test candidates for whether they can be divided by any of the primes in our list.

Note that if `n` has prime factors, either it is the perfect square of a prime, or it is the product of two prime factors, one of which is smaller than the square root of `n` and one larger.

*Proof*:  

Let `p` and `q` be two prime factors of `n` with `p` not equal to `q`.  

Let `f` be the square root of `n`, `f` is usually not integer.  We have that

```
n = f * f = p * q
```
Now, suppose that `q > f`.  Then
```
f * f = p * q > p * f
```

Dividing by `f`, it follows that `f > p`.

<p>&#x25A1;</p>


The important conclusion is that we need only check primes whose square is less than or equal to `n`.

Here is the code:

**script.py**

```
L = [2,3,5]

def test(n):
    print('test', n)
    assert n > 5
    D = dict()
    for p in L:
        if n % p == 0:
            return False
        if p in D:
            sq = D[p]
        else:
            sq = p*p
            D[p] = sq
        if sq > n:
            return True
    # we never reach this point
    print('error')
```

```
def next_prime():
    n = L[-1]
    n += 2
    while not test(n):
        n += 2
    L.append(n)

N = 10

for i in range(N):
    next_prime()
print(L)
```

```
> p3 script.py
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
```

We might also test if the last digit is 5 and skip those.  

#### Formatting

When printing out a large set of numbers it is helpful if the numbers are aligned in columns.  One approach is to take each number and convert it to a string of the same size.

To show this approach I will grab some random numbers smaller than 10000.  We'll set it up so that some are really small, some medium size and some large.

```
import random
random.seed(31)
N = 20

rL = list()
for i in range(N):
    for SZ in [100,1000,10000]:
        n = random.choice(range(SZ))
        rL.append(n)
random.shuffle(rL)

pL = [str(n).rjust(4) for n in rL]
for n in pL[:5]:
    print(n)
```

This prints:

```
> p3 script.py
 548
  18
 402
  67
3373
>
```

We know that the largest number will have at most four digits.  If we didn't know that, we could do `len(str(max(L)))`.  `max(L)` returns the largest value in the list.

Convert the maximum value to a string, and then get the length of that string.

The line `random.seed(31)` means we'll get the same numbers each time we run the script.  This is useful when testing.  Later, you could remove that line (or comment it out by putting a `#` in front).

The function `rjust(4)` puts additional spaces in front of the number to a maximum length of four.  `rjust` stands for "right-justification" (alignment).

#### Chunks

The next part of the problem is to break the list into chunks, according to the number of columns we want in the output.

There are various ways to do this.  The official way is to use the `itertools` module, but the syntax is awkward.  I think this is better.

Remove the `print` call at the end of what we had above, and replace it with this:

```
cols = 6  # columns
R = range(0,len(pL),cols)
pL = [pL[i:i+cols] for i in R]
for group in pL:
    print(' '.join(group))
```

which prints

```
> p3 script.py
 548   18  402   67 3373  788
 401  480 2272  364  542   44
1935   76  741 6167 2207   88
3357   14  976  978   97  548
6601   43 5978    1  203 2307
3554 8968 3797   62   87   26
2237   53  422   42   26   84
   7  758 1841    2 2287    3
  29   91 7335  598   75  844
8703  775   23 4039   95  151
>
```

When `#` appears in a line, it signifies a comment, anything in the line after that character is ignored by Python.

#### Sieve of Eratosthenes

Wikipedia [article](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

We will construct a list of boolean values (`True` or `False`).  `L[i]` will be `True` when the integer `i` is a prime number, and `False` otherwise.

To do this, first start with a list that contains `[False, False, True ...` with all subsequent values `True`.  

Then mark the indexes that correspond to multiples of `2` as `False`.  Next, mark those that are multiples of `3` as `False`, and so on.  But only carry out this "clear" operation for integers that are prime.

```
import math
L = [False,False] + [True]*24
N = len(L)

def clear(n):
    f = n + n
    while f < N:
        L[f] = False
        f += n

top = int(math.sqrt(N))
for n in range(top+1):
    if L[n]:
        clear(n)

pL = [i for i in range(N) if L[i]]
print(pL)
```

```
> p3 script.py
[2, 3, 5, 7, 11, 13, 17, 19, 23]
>
```

Note that it is only necessary to do this for `i` less than or equal to the square root of the largest value.

Also, we implement the operation using only addition rather than multiplication.
