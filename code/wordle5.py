import sys, random, collections

h = 'call the script as in:\npython3 my_wordle.py <n>\n'
h += 'n = difficulty, range (1-10)'
if '-h' in sys.argv or '--help' in sys.argv:
    print(h)
    sys.exit()

def load_data(fn):
    p = '/Users/telliott/Dropbox/Github'
    p += '/Python3Intro/data/'
    with open(p+fn) as fh:
         data = fh.read()
         
    # 5-letter words from Norvig's database
    # ranked by frequency, most to least common
    return data.strip().split('\n')

fn = 'words5.txt'
L = load_data(fn)
N = 500

delta = 1
if len(sys.argv) == 2:
    try:
        delta = int(sys.argv[1])
    except:
        delta = 2
    N *= delta
    
# --------------------------------

print()
print("I'm thinking of a 5-letter word")
print('Want to guess?')
print('<q> to quit\n<h> for help')
print()

correctD = dict()
guessD = collections.defaultdict(list)

keyboard = '''
Q W E R T Y U I O P
 A S D F G H J K L
Z X C V B N M'''

kb = keyboard
hr = '-'*30 # horizontal rule

# --------------------------------
# target
t = random.choice(L[:N])

sL = list('.....')
counter = 0

def handle(r):
    global counter
    if r in ['h','help']:
        print(h)
        print("letters marked as correct may match twice")
        return
    
    counter += 1
    r = r.strip().lower()
    print("guess no. %d      %s" % (counter,r))
    
    if not r in L:
        print("that doesn't seem to be a valid 5-letter word\nplease try again")
        print(hr)
        return
    
    correct = r == t

    # kb prints the keyboard (minus letters guessed)
    global kb, sL
    
    # remove guessed chars from the keyboard
    for c in r:
        kb = kb.replace(c.upper(),' ')
    
    # central logic
    for i,(x,y) in enumerate(zip(r,t)):
    
        # sL holds exact matches at each index
        if x == y:
            sL[i] = x
            
        # guessD holds indices where that char has been guessed (incorrectly)
        if x != y and x in t:
            guessD[x].append(i)     
    
    # print exact matchline
    print('matched:         %s' % ''.join(sL))
    if correct:  
        return True
    
    # go through guesses in alphabetical order
    # skipping those that were correct
    kL = [k for k in sorted(guessD.keys()) if not k in sL]
    
    # for each char guessed incorrectly
    for i,c in enumerate(kL):
    
        # for each c, guessD[c] holds list of positions
        iL = guessD[c]
        pL = list()
        
        # build the list that holds positions guessed
        for j in range(5):
            # for this char, if guessed at this position, note it
            if j in iL:
                pL.append(c)
            # otherwise just put '.'
            else:
                pL.append('.')
        
        # do not repeat the 'out of place:' part
        if i == 0:      
            print('out of place:    %s' % ''.join(pL))
        else:
            print('                 %s' % ''.join(pL))
        
        # should we note repeated chars?

    print(kb.rstrip())
    print(hr)

# --------------------------------

while True:
    r = input('=> ')
    if r in ['q','quit']:
        if counter > 1:
            print("the word was %s" % t)
        sys.exit()
    correct = handle(r)
    if correct:
        print('congratulations')
        break
    
print("the word was %s" % t)

score = (delta/counter) * 50
t = (delta,counter,int(score))
print('difficulty = %d, %d rounds, score = %d' % t)

