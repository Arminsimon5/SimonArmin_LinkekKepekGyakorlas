import math

#1.feladat
print("1.feladat")
krumpliAr = int(input("Mennyibe kerül 1 kg krumpli? "))
mennyiKell = int(input("Hány kg-ot szeretne venni?" ))
print(krumpliAr * mennyiKell,"forintot kell magával vinni.")

#2.feladat
print("\n\n2.feladat")
jelenlegiFiz = int(input("Mennyi a jelenlegi fizetése? "))
emelesSzaz = int(input("Hány százalékos emelést kap? "))
szorzoszam = emelesSzaz / 100 +1
print(jelenlegiFiz * szorzoszam,"forint lesz a fizetés emelés után a fizetése.")

#3.feladat
print("\n\n3.feladat")
felrerakPenz = int(input("Hány forintot tud félrerakni havonta? "))
laptopAr = int(input("Hány forintba kerül a kiválasztott laptop? "))
print(laptopAr / felrerakPenz,"hónapot kell spórolnia." )

#4.feladat
print("\n\n4.feladat")
kolcsonOssz = int(input("Hány forintot vett fel köcsönbe? "))
futamido = int(input("Hány évre vedte fel? "))
print(kolcsonOssz / futamido, "forintot kell éventevissza fizetnie.")

#5.feladat
print("\n\n5.feladat")
szobaSzel = int(input("Hány méter széles a szoba? "))
szobaMag = int(input("Hány méter magas a szoba? "))
szobaKobmeter = szobaSzel * szobaMag 
print(szobaKobmeter / 0.04,"darab csempe kell a falhoz")


#6.feladat
print("\n\n6.feladat")
ido1Ora = int(input("Add meg az első időpont óráját.")) 
ido1Perc = int(input("Add meg az első időpont percét."))
ido1MPerc = int(input("Add meg az első időpont másodpercét."))
ido2Ora = int(input("Add meg az második időpont óráját.")) 
ido2Perc = int(input("Add meg az második időpont percét."))
ido2MPerc = int(input("Add meg az második időpont másodpercét."))
ido1 = ido1Ora*3600+ido1Perc*60+ido1MPerc
ido2 = ido2Ora*3600+ido2Perc*60+ido2MPerc
idoKul = ido1 -ido2
if(idoKul >-1):
    print(idoKul,"mp a két időpont közötti különbség.")
else:
    print(ido2 - ido1,"mp a két időpont közötti külonbség")

#7.feladat
print("\n\n7.feladat")
dinnyeAtmero = int(input("Hány cm a dinnye átmérője?"))
dinnyeDarab = int(input("Hány dinnye van?"))
dinnyeAtMeter = dinnyeAtmero /100
print((dinnyeAtMeter+0.6)*dinnyeDarab,"méter szalag kell.")

#8.feladat
print("\n\n8.feladat")
kertHossz = int(input("Hány méter a kert hossza? "))
kertSzel = int(input("Hány méter a kert szélessége? "))
kertMeret = kertHossz * kertSzel
print(math.ceil(kertMeret/5)," darab fűmagot kell venni.")

#9.feladat
print("\n\n9.feladat")
egesz1 = int(input("Adjon meg egy egész számot!"))
egesz2 = int(input("Adjon meg mégegy egész számot!"))
print(math.sqrt(egesz1+egesz2)," a két szám négyzetgyöke.")

#10.feladat
print("\n\n10.feladat")
szam = float(input("Adjon meg egy pozitív valós számot. "))
print("A megadott szám a",math.floor(szam),"és a",math.ceil(szam),"egész számok között van, és ezek közül a",round(szam),"számhoz van közelebb.\n a szám egész része:",)


#11.feladat
print("\n\n11.feladat")
valos = float(input("Adjon meg egy valós számot."))
print(valos)