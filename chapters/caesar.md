#### Caesar Cipher

Julius Caesar famously used a technique for encryption that replaces each letter of the alphabet by the letter that comes 3 places after it.  `A => D` and so on.

At the end of the alphabet, we wrap around so that `X => A`, `Y => B` and `Z => C`.

An easy way to implement this system is to construct a dictionary which maps plaintext letters to ciphertext letters.  An advantage is that a reverse dictionary swapping the values and keys can then be usedd to decrypt.

Here is a somewhat fancy way to construct the dictionary.

**script.py**

```
import sys

def make_dict():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    fD = dict()
    for i,k in enumerate(letters):
        try:
            value = letters[i+3]
        except IndexError:
            value = letters[i+3-26]
        fD[k] = value
    fD[' '] = ' '
    return fD

def make_rev_dict(fD):
    rD = dict()
    for k in fD:
        rD[fD[k]] = k
    return rD
```

We "handle" the `IndexError` that occurs for the three letters at the end of the alphabet.

However, in this particular case it can all be done more simply, with two lists.

**script.py**

```
import sys

def make_dicts():
    L1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    L2 = 'XYZABCDEFGHIJKLMNOPQRSTUVW '
    
    fD = dict(zip(L1,L2))
    rD = dict(zip(L2,L1))
    return fD,rD
    
def convert(s,D):
    rL = [D[c] for c in s]
    return ''.join(rL)
    
fD,rD = make_dicts()
    
text = sys.argv[1].upper()
print(text)
    
enc = convert(text,fD)
dec = convert(enc,rD)
print(enc)
print(dec)
```

```
> p3 script.py "Gallia est omnis divisa in partes tres"
GALLIA EST OMNIS DIVISA IN PARTES TRES
DXIIFX BPQ LJKFP AFSFPX FK MXOQBP QOBP
GALLIA EST OMNIS DIVISA IN PARTES TRES
>
```

#### A bit more sophistication

There are a couple problems with the first solution.  One is that the spacing in the plaintext is retained in the ciphertext.  Normally, the way to deal with that is to eliminate the spacing in the original and group the letters in 5-letter words:

`GALLIA EST OMNIS DIVISA IN PARTES TRES`

becomes

`GALLI AESTO MNISD IVISA INPAR TESTR ES`

Another problem is that `A` is always encoded as `D`, and so on.

We could do this instead:

```
ABCDEF...
BCDEFG...
CDEFGH...
DEFGHI...
EFGHIJ...
...
```

And then pick the two lists to use according to some scheme, perhaps based on a password or passphrase.

This is called a Vigenère square or table.  We can do better.

Here is a dictionary where the mapping is to a random permutation:

```
import random
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def make_dicts():
    L1 = list(letters)
    L2 = L1[:]
    random.shuffle(L2)
    fD = dict(zip(L1,L2))
    rD = dict(zip(L2,L1))
    return fD,rD

fD,rD = make_dicts()
L = [fD[c] for c in letters]
print(''.join(L))
```

```
> p3 script.py
FSZNHRPUXLIGKAYBDTEMCQVOWJ
>
```

To be useful, we need a way of getting the same permutation for the same position every time, depending only on the passphrase.

This can be done with `random.seed`:

```
import random
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def scrambled_dicts(pw):
    random.seed(pw)
    L1 = list(letters)
    L2 = L1[:]
    random.shuffle(L2)
    fD = dict(zip(L1,L2))
    rD = dict(zip(L2,L1))
    return fD,rD

fD,rD = scrambled_dicts(231)
L = [fD[c] for c in letters]
print(''.join(L))
```

```
> p3 script.py
ICDUQZPBTYWRLFXONJVGHSKMEA
> p3 script.py
ICDUQZPBTYWRLFXONJVGHSKMEA
>
```

So then we can sketch a solution.  Convert a password into a sequence of integers.  Use each one to set the seed when generating a scrambled dictionary.

```
import sys, random
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def make_dicts(n):
    random.seed(n)
    L1 = list(letters)
    L2 = L1[:]
    random.shuffle(L2)
    fD = dict(zip(L1,L2))
    rD = dict(zip(L2,L1))
    return fD,rD

pw = 'supersecretpw'
iL = [i*ord(c) for i,c in enumerate(pw)]
print(iL)

L = []
for i in iL:
    fD,rD = make_dicts(i)
    L.append((fD,rD))
    
ptext = 'ATTACKATDAWN'
ctext = [L[i][0][c] for i,c in enumerate(ptext)]
print(''.join(ctext))
dtext = [L[i][1][c] for i,c in enumerate(ctext)]
print(''.join(dtext))
```

```
> p3 script.py
[0, 117, 224, 303, 456, 575, 606, 693, 912, 909, 1160, 1232, 1428]
ORDPSLWWPFMC
ATTACKATDAWN
>
```

Notice that `A` is encoded variously as one of `OPWF`, also that `P` encodes both of `AD` and `W` encodes both of `AT`.

For the future:  make sure the possible values for the seed exceed the length of the plaintext.  We could maybe use the 256 bit hash of the passphrase, for short to medium-sized messages.

You may have other ideas if you read about the Python `secrets` module.