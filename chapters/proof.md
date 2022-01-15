#### Proof of work

The blockchain has a notion called proof-of-work.

To explain what this is, let's start by defining a **digital object** as anything that can be represented by a sequence of digits:  whether it's a text file or a png image, a Python script, or even a compiled C program.

A digital object is composed of digits that can be viewed (in different bases) as binary or decimal or hexadecimal digits, but any such object is also at the same time simply a large (often gigantic) number.

#### hashing

A **hash function** is a *one-way* function.  You feed in a digital object (of any size) and out comes a digital object of a fixed size.  Originally a hash called `md5` was popular, today `sha256` is common.

The hashes computed by the md5 function have 32 hexadecimal (hex) digits (16 bytes, 96 bits), sha1 is 40 hex digits (20 bytes, 160 bits), while the sha256 function has 64 hexadecimal digits (32 bytes, 256 bits), hence the name of the latter.

These functions are available in the shell (`zsh`) run by Terminal:

```
> printf 'abc' > x.txt
> hexdump x.txt
00000000  61 62 63                                          
00000003
>> md5 x.txt
MD5 (x.txt) = 900150983cd24fb0d6963f7d28e17f72
> printf 'abc' | md5  
900150983cd24fb0d6963f7d28e17f72
>
```

Both `md5` and the `openssl` suite come with macOS.

A hash function is one-way (or "trapdoor").  If all you know is the output, you can't say anything about the input. There is no way to know which digital object to input in order to match any given output hash.

Given the input, it is very easy to obtain the hash and very fast.

There is the theoretical possibility of a *collision*, which is the situtation that two digital objects have the same hash.  The `md5` hash is 96 bits.  2^96 is almost 10^29.  If we constructed random objects with more than 96 bits, then obviously some of them must have the same hash.  But this is obviously a remote possibility.  

256 bits is about 10^77.  If we assume that (on average) every star in the universe has the same number of atoms as our sun, then the number of atoms in the universe is about 10^57 x 10^11 x 10^11 = 10^79.

Note:  if one knows (or suspects) the data to be very short, it should be possible to guess all possible values of the data.  Also the data is padded to have a specified length (for MD5 this is 448 mod 512).  To this is added a 64-bit value representing the length of the original data.

#### proof-of-work

As a **bitcoin miner** one constructs blocks, which are collections of "transactions", to form a digital object.  A block also includes a digital object (a number) called a **nonce**, which is just some random data, but you want data that confers on the block a rare property.  

The rare property is that the hash of the block is a very small number in the universe of 256-bit numbers.  

As a result, the hash has some specified number of leading zeroes.  Since it is difficult to find a nonce with this property, the rarity shows that you put some computational effort into discovering it.  The only way to find such a nonce is to try many, many times, randomly.

Here is a script to model that process.

```
import sys, hashlib, time 

data = sys.argv[1]
t = '0' * int(sys.argv[2])

def one_run():
    start = time.time()
    m = hashlib.sha256()
    m.update(data.encode('UTF-8'))
    i = 0
    while True:
        i += 1
        c = m.copy()
        c.update(str(i).encode('UTF-8'))
        h = str(c.hexdigest())
        if h.startswith(t):
            x = '%10.4f' % (time.time() - start)
            s = str(i).rjust(10)
            print(x,s,h[:20] + '...')
            break

one_run()
```

```
script.py
> p3 script.py mydata 4
    0.0984      79246 00001bd85ce60d6abe40...
> p3 script.py mydata 5
    1.8948    1610357 00000dc787a1c2eebe04...
> p3 script.py mydata 6
  107.7354   85086374 000000e3bd19eb091681...
>
```

We start with input data, which here is just "mydata".  Then we figure out which number, when added to the data, results in a hash starting with the specified number of leading zeros.

The first value in the output is the time elapsed (in seconds), followed by the nonce which was actually used, and the third is the sha256 hash of the resulting digital object.

Note the non-linearity.  There is a factor of 16 at each stage, so the difference between 4 leading zeroes and 6 is only a factor of 16 squared, but the difference in time was more than a factor of 1000.  Sometimes you're lucky, and sometimes you're not.

The hash of the latest block on the Bitcoin blockchain (as I write) is as follows:

```
00000000000000000002a72faf4e6793b4c6fc0b8d1fda44339e5ba7d5b7c753
```

The hash of the first (genesis) block of Bitcoin is:

```
000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```
