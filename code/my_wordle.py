import sys, random, collections

def load_data(fn):
    p = '/Users/telliott/Dropbox/Github'
    p += '/Python3Intro/data/'
    with open(p+fn) as fh:
         data = fh.read()   
    # 5-letter words from Norvig's database
    return data.strip().split('\n')

fn = 'norvig5.txt'
L = load_data(fn)

N = 500
delta = 1
if '-m' in sys.argv:
    i = sys.argv.index('-m')
    try:
        delta = int(sys.argv[i+1])
    except:
        delta = 2
    N *= delta
    
if '-h' in sys.argv or '--help' in sys.argv:
    print('flags: `-m <n>` increases the difficulty')
    sys.exit()

# --------

# target
t = random.choice(L[:N])

p = "Wordle\nI'm thinking of a 5-letter word\n"
p += "Want to guess?\n"
p += 'level: %d\n' % delta
p += "enter q to quit\n\n"

correctD = dict()
guessD = collections.defaultdict(list)

keyboard = '''
     Q W E R T Y U I O P
      A S D F G H J K L
     Z X C V B N M
'''

kb = keyboard
hr = '-'*30 # horizontal rule

# --------

sL = list('.....')


def handle(r):
    r = r.strip().lower()
    print("guess:          %s" % r)
    if not r in L:
        print("that doesn't seem to be a valid 5-letter word\nplease try again")
        return
    
    correct = r == t

    global kb, sL  
    for c in r:
        kb = kb.replace(c.upper(),' ')
    
    for i,(x,y) in enumerate(zip(r,t)):
        if x == y:
            sL[i] = x            
        if x != y and x in t:
            guessD[x].append(i)
                       
    print('matched:    ')
    print('                %s' % ''.join(sL))
    
    if correct:  
        return True
    
    kL = [k for k in sorted(guessD.keys()) if not k in sL]
    #print('present: (%s)' % ''.join(kL))
    print('out of place:')
    for c in kL:
        iL = guessD[c]
        pL = list()
        for i in range(5):
            if i in iL:
                pL.append(c)
            else:
                pL.append('.')
        print('                %s' % ''.join(pL))

    print('to try:')
    print(kb)
    print(hr)

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

    correct = handle(r)
    if correct:
        print('congratulations')
        break
    
print("the word was %s" % t)
