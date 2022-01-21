#### Sorting

A common task is to sort a list of values into ascending order.  Often, the reason is so that we can efficiently search the list to see whether it contains a particular value.

We can do this for any values that have a sense of ordering,whether it is just ints or floats, or strings with lexicographical sorting:  `'a' < 'b'` and so on.

#### Get yer random numbers

To start, let's generate some random integers and then print them.

**script.py**

```
import random

SZ = 10
L = [random.randint(0,100) for i in range(SZ)]
print(L)
```

```
> p3 script.py
[98, 24, 24, 78, 28, 31, 54, 62, 92, 7]
> p3 script.py
[46, 78, 72, 21, 29, 93, 82, 55, 85, 36]
>
```

The `random` module has a function `randint` that generates random integers in a given range.  (For some reason, this range includes the high value, unlike we usually see with Python).

It's often a good idea to work with the *same* "random" input until we get everything working.  Calling `random.seed()`, to "seed" the random number generator, will do that.

Add to the script:

```
random.seed(151)
```

Now

```
> p3 script.py
[90, 52, 91, 80, 92, 26, 45, 36, 47, 73]
> p3 script.py
[90, 52, 91, 80, 92, 26, 45, 36, 47, 73]
>
```

#### Sorting

Here's one approach.  We make a second list and grab values from the first list in order.

```
def selection_sort(input):
    L = input[:]
    rL = list()
    while L:
        x = min(L)
        L.remove(x)
        rL.append(x)
    return rL
```

We make a copy of the input list with `L = input[:]`, because we are going to modify the data and don't want to propagate the changes outside this function.

We can see that issue in this snippet from the interpreter:

```
>>> L = [1,2,3]
>>> def f(input):
...      input[0] = 0
... 
>>> f(L)
>>> L
[0, 2, 3]
>>>
```

The change inside the function `f` was propagated to `L`, which was defined *outside* `f`.

This happens with lists but not with, say, ints.

```
>>> n = 10
>>> def f(n):
...     n += 1
...     print(n)
... 
>>> f(n)
11
>>> n
10
>>>
```

Back to sorting.  After making the copy we simply identify the smallest number remaining in the list at each stage, remove it, and add it to the end of a new list.  When there are no more elements to remove, we're done.

`min` is a built-in function which finds the minimum value.  It even works on strings:

```
>>> L = list('abc')
>>> min(L)
'a'
>>> L2 = ['ab','bc']
>>> min(L2)
'ab'
>>>
>>> nax(L2)
'bc'
>>>
```

The big problem with our code that `L.remove(x)` is expensive.

We *could* build a different data structure (a linked list) for which removal would be easy, but that's for another time.

We could also build the modified list leaving out `x`, ourselves:

```
    while L:
        x = min(L)
        i = L.index(x)
        L = L[:i] + L[i+1:]
        rL.append(x)
```


#### Selection sort

An alternative approach is to carry out an in-place sort, that is, modify the original list to hold the results.  We do this by defining a `swap` function to exchange the values at two different positions.

Here is an approach that works:

```
import sys, random
random.seed(151)

SZ = 10
L = [random.randint(0,100) for i in range(SZ)]
print(L)

def swap(i,j):
    L[i],L[j] = L[j],L[i]

N = len(L)
count = 0

for i in range(N-1):
    for j in range(i+1,N):
        if L[i] > L[j]:
            swap(i,j)
            print(L)
            count += 1

print(count)
```

```
[90, 52, 91, 80, 92, 26, 45, 36, 47, 73]
[52, 90, 91, 80, 92, 26, 45, 36, 47, 73]
[26, 90, 91, 80, 92, 52, 45, 36, 47, 73]
...
[26, 36, 45, 47, 52, 73, 80, 90, 91, 92]
28
>
```

I have cut out some of the output and replaced it with `...`.

The first two swaps are `90<->52` and then `52<->26`.  After each call to `swap`, we reload the values at indexes `i` and `j`.  

As a result, after the first time through the inner loop, `for j in ..`, the minimum value in the list is placed correctly.

The problem is that this takes *a lot* of swaps.

The algorithm is called **selection sort**.  


A variation would be to first find the smallest element in the range `i+1:SZ` and then only swap that one with the element at `i+1`.  That would avoid some swaps, but it still takes a lot of comparisons.

```
def selection_sort(input):
    L = input[:]
    SZ = len(L)
    for i in range(SZ-1):
        current = L[i]
        next = min(L[i+1:])
        j = L.index(next)
        if current > next:
            L[i],L[j] = L[j],L[i]
        else:
            L[i+1],L[j] = L[j],L[i+1]
    return L 
```

This works, however, it has issues.  One is that it calls `L.index(next)`, which is somewhat expensive, when we might have saved the index already from a smarter implementation of `min`.

Other improvements could be made to the code, but this is a good place to stop.

There are plenty of sorting algorithms whose implementation is fairly easy and they are great practice for improving your Python skills.  These include:

- insertion sort
- merge sort
- quick sort

and many others.