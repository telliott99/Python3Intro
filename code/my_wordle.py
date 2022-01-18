'''
to do
adjust difficulty
analyze logic failures in main loop
'''


import random

#fn = 'sgb-words.txt'
fn = 'norvig5.txt'
p = '/Users/telliott/Dropbox/Github'
p += '/Python3Intro/data/'

with open(p+fn) as fh:
    data = fh.read()
    
# 5-letter words from Norvig's database
L = data.strip().split('\n')

# target
t = random.choice(L[:2000])

'''
fn = 'sgb-words.txt'
p = '/Users/telliott/Dropbox/Github'
p += '/Python3Intro/data/'

with open(p+fn) as fh:
    data = fh.read()
L = L + data.strip().split('\n')
'''

p = "Wordle:  guess the 5-letter word\n"
p += "enter q to quit\n\n"
gL = list()

keyboard = '''
Q W E R T Y U I O P
 A S D F G H J K L
Z X C V B N M
'''
kb = keyboard

# --------

def handle(r,gL):
    r = r.strip().lower()
    print("guess:   %s" % r)
    if not r in L:
        print("that doesn't seem to be a valid 5-letter word\nplease try again")
        return
    
    global kb
    rL = list()
    for c in r:
        kb = kb.replace(c.upper(),' ')
    
    for x,y in zip(r,t):
        if x == y:
            rL.append(x)
        else:
            rL.append('.')
            
        if x != y and x in t:
            gL.append(x)
    
    gL = list(set(gL))
    local_copy_gL = [c for c in gL if not c in rL]
            
    s =  'matches: %s ' % ''.join(rL)
    s += '(%s)' % ''.join(local_copy_gL)
    
    correct = r == t
    return correct, s

def debug(v = True):
    if v:
        print(e)
    else:
        print('an error occurred')

# --------

first_time = True

while True:
    if first_time:
        r = input(p)
    else:
        r = input('')
    first_time = False
    
    if r in ['q','quit']:
        break

    retval = handle(r,gL)
    if retval:
        correct,result = retval
        print(result)
        print(kb, '-'*20)
        
        if correct:
            print('congratulations')
            break
    
print("the word was %s" % t)


'''> p3 my_wordle.py
Wordle:  guess the 5-letter word
enter q to quit

aegis
guess:   aegis
matches: ..... (es)

Q W   R T Y U   O P
     D F   H J K L
Z X C V B N M
 --------------------
ounce
guess:   ounce
matches: ..... (es)

Q W   R T Y       P
     D F   H J K L
Z X   V B   M
 --------------------
wordy
guess:   wordy
matches: ..... (wes)

Q       T         P
       F   H J K L
Z X   V B   M
 --------------------
sawer
guess:   sawer
that doesn't seem to be a valid 5-letter word
please try again
barmy
guess:   barmy
matches: ..... (wes)

Q       T         P
       F   H J K L
Z X   V      
 --------------------
quite
guess:   quite
matches: ..... (wets)

                  P
       F   H J K L
Z X   V      
 --------------------
newts
guess:   newts
matches: ..... (wets)

                  P
       F   H J K L
Z X   V      
 --------------------
sweet
guess:   sweet
matches: swe.t ()

                  P
       F   H J K L
Z X   V      
 --------------------
sweat
guess:   sweat
matches: swe.t ()

                  P
       F   H J K L
Z X   V      
 --------------------
swept
guess:   swept
matches: swept ()

                   
       F   H J K L
Z X   V      
 --------------------
congratulations
the word was swept
>
'''