#elágazások
from datetime import date
import math
from traceback import print_last, print_list
#egyszerű egyírányú : ha (feltétel)--> utasítás
"""
if feltétel: -- ha az adott feltétel teljesül az if alatt lévő utasítás fog lefutni
    utasítás
else:        -- ha a feltétel nem teljesül(minden más esetben), akkor az else alatt lévő utasítás fut le
    utasítás
Mindaz, ami az if-hez tartozik(Ami a feltétel teljesülése után végre akarunk hajtani, az egy tabulátorral beljebb kell írni)    

egesz = int(input("Kérek egy egész számot: "))
if egesz < 0:
    print("A megadott szám negatív")
    print("A szám abszolútértéke: ", (-1*egesz))
elif egesz ==0:                 # ha több feltételem van elif után berakhatok újabb feltételeket.
    print("A szám nulla!")
else:                           # else mögé már nem teszünk feltételt 
    print("A megadott pozitív.")
    print("A szám abszolútértéke: ", egesz)

#logikai operátorok:
Logikai ÉS and: akkor igaz, ha mindkét feltétel igaz
Logikai VAGY or: akkor igaz, ha legalább az eggyik tag igaz
logikai tagadás negáció: not vagy !=
"""
#3.feladat

print("\n\n3.feladat")
egesz = int(input("Adjon meg egy egész számot."))
osztasimaradek = egesz%10
if osztasimaradek==0:
    print("A szám osztható 10-zel.")
else:
     print("A szám osztási maradéka: ",osztasimaradek)

#4.feladat
print("\n\n4.feladat")
egesz1=int(input("Adja meg a számlálót."))
egesz2=int(input("Adja meg a nevezőt."))
if egesz2 == 0:
    print("HIBA! A tört nevezője nem lehet nulla.")

#5.feladat
print("\n\n5.feladat")
haromjegyu = int(input("Adjon meg egy háromjegyű egész számot."))
szazas = math.floor(haromjegyu/100)
tizes = math.floor((haromjegyu%100)/10)
eggyes =(haromjegyu%100)%10
osszeg = szazas*szazas*szazas+tizes*tizes*tizes+eggyes*eggyes*eggyes
if haromjegyu== osszeg:
    print("Ez egy Armstrong szám.")
else:
    print("Ez nem egy Armstrong szám.")

#6.feladat
print("\n\n6.feladat")
szam = int(input("Adjon meg egy számot. "))
if szam==4:
    print("A megadott szám 4-es.")
if szam<10:
    print("A megadott szám kissebb, mint 10.")
if szam%2 == 0:
    print("A megadott szám páros.")
if szam<11 and szam>-1:
    print(" A megadott szám a [0,10] intervallumba esik.")
if szam%3 == 0 and szam%5 == 0:
    print("A megadott szám osztható 3-mal és 5-tel is.")
if szam<10 or szam>20:
    print("A megadott szám nem a [10,20] intervallumba esik.")
    

#7.feladat
print("\n\n7.feladat")
szam1 = int(input("Adjon meg egy egész számot. "))
szam2 = int(input("Adjon meg egy másik egész számot. "))
if szam1 == szam2:
    print("A két szám egyenlő.")
if szam1%2 == 1 and szam2%2 == 1:
    print("Mind két szám páratlan.")
if szam1%3 == 0 or szam2%3 == 0:
    print("Legalább az eggyik szám osztható hárommal")
if szam1<0 and szam2<0:
    print("Mind két szám negatív.")
if szam1<0 and szam2>-1:
    print("Az egyik szám negatív a másik szám pozitív.")
if szam2<0 and szam1>-1:
    print("Az egyik szám negatív a másik szám pozitív.")

#8.feladat
print("\n\n8.feladat")
a = int(input("Adja meg téglalap egyik oldalát."))
b = int(input("Adja meg téglalap másik különböző oldalát."))
if a==b:
    print("A megadott alakzat az négyzet.")
else:
    print("A megadott alakzat téglalap.")

#9.feladat
print("\n\n9.feladat")
a = int(input("Adja meg a háromszög első oldalát."))
b = int(input("Adja meg a háromszög második oldalát."))
c = int(input("Adja meg a háromszög harmadik oldalát."))
if a == b == c:
    print("Szabályos a háromszög")
else:
    print("Nem szabályos a háromszög.")

#10.feladat
print("\n\n10.feladat")
szam = int(input("Adjon meg egy egész számot. "))
if szam==10:
    print("A szám egyenlő tizzel")
elif szam==100:
    print("A szám egyenlő százzal.")
elif szam==1000:
    print("A szám egyenlő ezerrel.")
else:
    print("A szám nem egyenlő tizzel, százzal vagy ezerrel.")

#11.feladat
print("\n\n11.feladat")
szam = int(input("Adjon meg egy egész számot. "))
if szam>0 and szam<10:
    print("A szám benne van az [1,9] intervallumban.")
else:
    print("A szám nincs benne az [1,9] intervallumban.")

#12.feladat
print("\n\n12.feladat")
szam = int(input("Adjon meg egy egész számot. "))
if szam%2 !=0 and szam<0:
    print("A szám negatív és páratlan.")
else:
    print("A szám pozitív vagy páros .")

#13.feladat
print("\n\n13.feladat")
szam1 = int(input("Adjon meg egy egész számot. "))
szam2 = int(input("Adjon meg egy másik egész számot. "))
if szam2%szam1 ==0:
    print("Az első szám osztója a második számnak.")
else:
    print("az első szám nem osztója a második számnak.")

#14.feladat
print("\n\n14.feladat")
szam = int(input("Adjon meg egy egész számot. "))
if szam<0:
    print("HIBA! Csak pozitív számok esetén értelmezett a gyökvonás.")
else:
    print("A szám gyöke:",math.sqrt(szam))

#15.feladat
print("\n\n15.feladat")
hszog1 = int(input("Adja meg a háromszög első oldalát. "))
hszog2 = int(input("Adja meg a háromszög második oldalát. "))
hszog3 = int(input("Adja meg a háromszög harmadik oldalát. "))
if hszog1 >0 and hszog2 >0 and hszog3 >0:
    print("A háromszög kerülete:",hszog1+hszog2+hszog3)
else:
    print("Hibás adatok...")

#16.feladat
print("\n\n16.feladat.")
hanykm = int(input("Hány kilométert tett meg? "))
mennyido = int(input("Hány óra alatt? "))
kmora = hanykm / mennyido
if kmora>=80 and kmora<=145:
    print("Minden rendben.")
else:
    print("Nem megfelelő sebességgel közlekedett.")

#17.feladat
print("\n\n17.feladat")
szam = int(input("Adjon meg egy egész számot. "))
if szam>0:
    print("A szám pozitív.")
elif szam<0:
    print("A szám negatív.")
else:
    print("A szám nulla.")

#18.feladat
print("\n\n18.feladat")
szam1 = int(input("Adjon meg egy egész számot. "))
szam2 = int(input("Adjon meg egy másik egész számot. "))
if szam1 > szam2:
    print(szam1,"nagyobb, mint",szam2)
elif szam1 < szam2:
    print(szam1,"kissebb, mint",szam2)
else:
    print(szam1,"egyenlő",szam2)

#19.feladat
print("\n\n19.feladat")
homerseklet = int(input("Adja meg a víz hőmérsékletét. "))
if homerseklet<0:
    print("szlárd (jég)")
elif homerseklet>=100:
    print("légnemű (gőz)")
else:
    print("folyékony (víz)")

#20.feladat
print("\n\n20.feladat")
szam1 = int(input("Adja meg az x tengelyt. "))
szam2 = int(input("Adja meg az Y tengelyt. "))
if szam1>0 and szam2>0:
    print("Első síknegyed")
if szam1>0 and szam2<0:
    print("Negyedik síknegyed")
if szam1<0 and szam2>0:
    print("Második síknegyed")
if szam1<0 and szam2<0:
    print("Harmadik síknegyed")

#21.feladat
print("\n\n21.feladat")
pSz = int(input("Adja meg a dolgozat pontszámát."))
if pSz>=0 and pSz<43:
    print("Elégtelen")
if pSz>=43 and pSz<58:
    print("Elégséges")
if pSz>=58 and pSz<73:
    print("Közepes")
if pSz>=73 and pSz<88:
    print("Jó")
if pSz>=88 and pSz<101:
    print("Jeles")

#22.feladat
print("\n\n22.feladat")
eletkor = int(input("Adja meg az életkort."))
if eletkor>=0 and eletkor<=13:
    print("Gyerek")
if eletkor>=14 and eletkor<=17:
    print("Fiatalkorú")
if eletkor>=18 and eletkor<=23:
    print("Ifjú")
if eletkor>=24 and eletkor<=59:
    print("Felnőtt")
if eletkor>=60:
    print("Idős")

#23.feladat
print("\n\n23.feladat")
tSur = int(input("Adja meg az tárgy sűrűségét."))
fSur = int(input("Adja meg a folyadék sűrűségét."))
if tSur>fSur:
    print("A tárgy elmerül.")
if tSur<fSur:
    print("A tárgy lebeg.")
if tSur == fSur:
    print("A tárgy úszík.")

#24.feladat
print("\n\n24.feladat")
igazolatlan = int(input("Adja meg az igazolatlan órák számát."))
if igazolatlan == 0:
    print("5")
if igazolatlan >= 1 and igazolatlan<=3:
    print("4")
if igazolatlan >= 4 and igazolatlan<=9:
    print("3")
if igazolatlan >= 10:
    print("2")
    szulEv = int(input("Adja meg a diák születési évét."))
    if szulEv>2022-18:
        print("Szülői értesítés szükséges.")
    else:
        print("Felszólítás kiküldése szükséges.")

#25.feladat
print("\n\n25.feladat")
kar = input("Adjon meg egy karaktert. ")
karASCII = ord(kar)
print(karASCII)
if karASCII>=48 and karASCII<=57:
    print("Szám.")
if karASCII>=65 and karASCII<=90:
    print("Nagy angol ABC betű.")
    print("Kis betűs alakja:",kar.lower())
if karASCII>=97 and karASCII<=122:
    print("Kis angol ABC betű.")
    print("Nagy betűs alakja:",kar.upper())
