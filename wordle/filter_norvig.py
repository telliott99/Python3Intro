# https://norvig.com/ngrams/

fn = "count_1w.txt"
with open(fn) as fh:
    data = fh.read()
data = data.strip().split('\n')

L = list()
for e in data:
    w,count = e.strip().split()
    if len(w) == 5:
        L.append(w)

print(len(L))

for i in range(0,len(L),500):
    print(str(i).rjust(5), ' '.join(L[i:i+10]))

fn = 'norvig5.txt'
with open(fn,'w') as fh:
    fh.write('\n'.join(L))
fh.close()

'''
> p3 script.py
39933
    0 about other which their there first would these click price
  500 costa trail buddy setup blues scope crazy bears mouth meter
 1000 wages males chaos wheat bases unity bride begun socks essex
 1500 cobra gucci threw https walsh ninth marry wills atoms drake
 2000 slips trays flock chung boris shave swamp faint gland blows
 2500 piles bezel havoc sling xoops rican gupta tummy axial julio
 3000 estes stomp norte glade licks caste libra lures slows lista
 3500 fryer namco garda marcy boron pauls riffs tetra vowed asher
 4000 grate orson wonka gorda alcoa jetzt fiend vespa enero yusuf
 4500 plist chemo krups honky muses freer toute oskar icici leans
 5000 beets betta repel emmet poste mello litas haart coyne hakim
 5500 zoids salas benji hsieh sayre cname dicom cielo laity imran
 6000 cleef inane ibsen asccm corky cgcgg yolks dello spook amped
 6500 monti jerzy seung adieu maida pawel snuck fanuc campy xlink
 7000 obeys kegel voile mysap kilim layed geyer ghazi citgo seiki
 7500 dasha akono liven huynh latta gohan spilt dunks wella terje
 8000 tamia regio wyden dawgs unita fukui ziply radko putts borse
 8500 onine carty aggro moria cantu hayne feely braff safin gilly
 9000 margi ginac fiera erate kurth copps cuppa tamas bugsy alief
 9500 shorn polak rhwng nomex fagor lande insel haram jebel josip
10000 harel cegui twigg ayant chics auron kaaza aledo vajra bartz
10500 nobly etana orage dever apoyo bunko hause nrcan marfa carmi
11000 kayne aimms skyfi avers anthy groks pudge baksh quale xmltv
11500 rowen otten ramah wixen leant domin ramis koepi ergot frama
12000 verbo morex wryly osten nayar polya ashly sigir redan regie
12500 bronc samco immed jeane minet bogut baldi vlado longe alcam
13000 criti shiel weren menke abord treed muggy arvid hauts aaeon
13500 movlw vejle manti inces fagus cafod valen lento holts kautz
14000 varla justa cobia monin kenia palas rebbi ucspi lavon nouba
14500 dynes mynix krack dunas mabon xawtv decls bloud mansi rhian
15000 hajar nicos szene orgel kiron xrefs vleck korey yajoo talla
15500 itive perea flurl qmake hrsdc dejar kurka holle ccaat fcsts
16000 ellon yware beato isced htonl raphy tokay munky ratan denti
16500 esham poket jaxon valin hynde hadde caird ngoss asaro nuded
17000 leuke gitte sodor tocca facer cahps chism brora gants lelie
17500 rubys vreme meche schob navid kisha hjelm vskip gaara ferne
18000 titlo eston zyvex kubby muira wispa geogr kassa hogle calcd
18500 goffe anism picta bajas gomme dayak yanik blyde aphra boote
19000 sylph iluka kacie moies clubb ricko fahmy delet hymne vinal
19500 cuddl mayde koryo ncome titov skiba rexec dquot taler prawo
20000 selpa issam taner heier dryed colca laube spiss algun eubie
20500 aquae doser puhca shome hoeft lueck schev dwsrf dijet aetec
21000 inits gulab jouse iname heter ambnt dundy hasil purls bounz
21500 grall timea saira divin asgnd grtis stabi meins kedit eanes
22000 jumer negar malig oneco ndrcd sdcfb salal hoyte koobi kalis
22500 miraz jimmi nucia lunen cewek ukirt nemko nasby oisin lcars
23000 alvan utans sanfl senet acaba ouchi ortec xicat bines eyres
23500 iolit malum whitd makki dacus talet vesid dhikr awaye macie
24000 hazem gywir piggs ligia daeth doink urwin abeka bcsia ilton
24500 oboks scutt klees iomem tihng pottr senay atool cisac refid
25000 nment ownik cauce skoob bisac ovest talke rifai imdur nauty
25500 kwzaa nqmes itxpo fsbos yllek wizip harrg golia ojkes haysi
26000 rnorm ifneq darse antya wowie stuey lotgd ginna folgt ebell
26500 zafra slika brays perca jezus avara phigs adutl winde becmg
27000 namdo denic nahas lalas galex thiam csfii bihan zollo genou
27500 richi gushy vexim rport whisp biull jafri ibeam andas pigza
28000 namei herrb palay balde condy adhes noori udipi eures faine
28500 infot gumbs davej vuxml shehu addys theys czeck allas dicha
29000 ayyub haena taire mdtrk kopje isong goral teela urrea deryk
29500 scrod armel tepic riolo halfe renos cddvd bable najwa hkcee
30000 cupsd aitel merli dweck amori ruegg xtech weste samie jtidy
30500 radev errin nessy brone sblog isfsi ecdsa yulan shoon budke
31000 narue kunga aklog sedxc uncom preme torys tiona sanny jakar
31500 beddy acson crile bozzo ushga lacsa tonex eskay samey pabon
32000 froms coamo laiho omdoc demio ducie jless zorki prpsc parki
32500 norin suero ralli fywyd entos usnrc emera putos ricke panni
33000 hudna citty aswat sikth campe moggi arrrr benzi kitka freke
33500 haner egpws mocie ibejo boake dorry proem dilek wtype sagoo
34000 thurl khris aytwn taake udrih pluby arnor swlug ekran pamie
34500 tatem kyrre hoche vetco ribsy alsey upaya niimi siirt retal
35000 exene selys cober barno shuja oatey mshda memek redig moena
35500 waemu menen ujima smsgt fiset shaff zygon naken cevin glave
36000 cellc ttbox moeck feind psset blsck grwnd eskog wujin iftop
36500 cande tansi curad askus neegu blust xpidl agoos fusty copcs
37000 kussa schek tronc sithe remes jimna calss totin sirte czard
37500 eated tohra mooga encik sarep xmlwf epipe rreal chuff proza
38000 robtv systs raphi woelk copni lback fusil cepat lytec langt
38500 memee bapti fiata madel inyri cpwhu vites russy teven goile
39000 rodby zakia maill kawas gpolo wnime msiac gotoo golor wholy
39500 filim bogoo maist gyool gopol goooh giogl fooal chike otoge
> 
'''