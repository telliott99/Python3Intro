#### Fun with the Genetic Code

**GeneticCode.py**

```
def get_GC_dict():

    aaL = ['FFLLSSSSYY**CC*W',
           'LLLLPPPPHHEERRRR',
           'IIIMTTTTNNKKSSRR',
           'VVVVAAAADDEEGGGG']
    
    aa = ''.join(aaL)  
        
    s = 'UCAG'
    codons = [x+y+z for x in s for y in s for z in s]
    return dict(zip(codons,list(aa)))
```
We need to explain that list comprehension:

```
>>> s = 'UCAG'
>>> [z for z in s]
['U', 'C', 'A', 'G']
>>> [y+z for y in s for z in s]
['UU', 'UC', 'UA', 'UG', 'CU', 'CC', 'CA', 'CG', 'AU', 'AC', 'AA', 'AG', 'GU', 'GC', 'GA', 'GG']
>>>
```

`[for y in s for z in s]` iterates `y` through `'UCAG'` in order, and then iterates `z` through `UCAG` in order, *for each* `y`.  The construct with `x + y + z` just extends this to the triplets.

We make a `dict` from the two lists with

```
dict(zip(codons,list(aa)))
```

The fun comes when we reverse the roles of keys and values and make a new dictionary.  

```
import GeneticCode
from collections import defaultdict

GC = GeneticCode.get_GC_dict()

def reverse_dict(D):
    rD = defaultdict(list)
    for k in D:
        v = D[k]
        rD[v].append(k)
    return rD
    
rGC = GeneticCode.reverse_dict(GC)
for k in sorted(rGC.keys()):
    print(k,rGC[k])
```

Normally, if we do `D[k]` with `k` not previously defined through `D[k] = v`, it's an error.  A `defaultdict` gives a default value for keys not previously added to the dictionary, here, an empty list.

Output:

```
> p3 script.py
* ['UAA', 'UAG', 'UGA']
A ['GCU', 'GCC', 'GCA', 'GCG']
C ['UGU', 'UGC']
D ['GAU', 'GAC']
E ['CAA', 'CAG', 'GAA', 'GAG']
F ['UUU', 'UUC']
G ['GGU', 'GGC', 'GGA', 'GGG']
H ['CAU', 'CAC']
I ['AUU', 'AUC', 'AUA']
K ['AAA', 'AAG']
L ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG']
M ['AUG']
N ['AAU', 'AAC']
P ['CCU', 'CCC', 'CCA', 'CCG']
R ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
S ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC']
T ['ACU', 'ACC', 'ACA', 'ACG']
V ['GUU', 'GUC', 'GUA', 'GUG']
W ['UGG']
Y ['UAU', 'UAC']
>
```