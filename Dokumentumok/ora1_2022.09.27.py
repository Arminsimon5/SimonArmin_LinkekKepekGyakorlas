from difflib import diff_bytes
import random
def f(szam):
    print("\n\n",szam,"feladat")

def f1():
    f(1)
    print(random.randint(0,10))
    print(random.randint(10,15))
    print(random.randint(0,100))
    print(random.randint(-100,100))
    for i in range(10):
        print(random.randint(0,1))
    for i in range(4):
        print(random.randint(-10,30))

def f2():
    f(2)
    tipp = int(input("Feldobok egy érmét.\nFej = 0;\nÍrás = 1;\nAdja meg a tippjét. "))
    tovabb = False
    while not tovabb:
        eredm = random.randint(0,1)
        if eredm == 0:
            print("Fej")
        else:
            print("Írás")
        if tipp==eredm:
            print("Jó a tipped.")
            tovabb = True
        elif tipp!=eredm:
            print("A tipped rossz.")
            ujra = input("Szeretnéd újra próbálni? Ha igen, írd be a konzolba.")
            if ujra == "igen":
                print("Akkor feldobom újra")
                tipp = int(input("Adja meg a tippjét.: "))
            else:
                tovabb = True

def f4():
    f(4)
    bekert = 1
    ossz = 1
    while bekert != 0:
        bekert = int(input("Adjon meg egy számot. "))
        ossz*=bekert
        print(ossz)

def f5():
    f(5)
    szoveg = "alma"
    bekert = input("Adjon meg egy szót.: ")
    while bekert != "":
        szoveg+=" "+bekert
        print(szoveg)
        bekert = input("Adjon meg egy szót.: ")

def f6():
    f(6)
    darab = int(input("Adjon meg egy számot. "))
    karakter = input("Adjon meg egy karaktert. ")
    szamlalo = 0
    while szamlalo != darab:
        print(karakter)
        szamlalo+=1

def f7():
    f(7)
    egesz1 = int(input("Adjon meg egy számot. "))
    egesz2 = int(input("Adjon meg egy másik számot. "))
    lepeskoz = int(input("Adja meg a lépéslözt"))
    szamlalo = 0
    kulonb = 0
    if egesz1 > egesz2:
        kulonb = (egesz1-egesz2)/lepeskoz
        print(egesz2)
        while szamlalo!=kulonb:
            print(egesz2+lepeskoz)
            egesz2+=lepeskoz
            szamlalo+=1
    elif egesz1 < egesz2:
        kulonb = (egesz2-egesz1)/lepeskoz
        print(egesz1)
        while szamlalo!=kulonb:
            print(egesz1+lepeskoz)
            egesz1+=lepeskoz
            szamlalo+=1

def f8():
    f(8)
    szamlalo=0
    while szamlalo<1001:
        if szamlalo%3==0 and szamlalo%5==0:
            print(szamlalo)
        szamlalo+=1

def f9():
    f(9)
    bekert = int(input("Adja meg az összeget.: "))
    osszeg=bekert
    ezres= 0
    otszaz= 0
    ketszaz= 0
    szaz = 0
    otven = 0
    husz = 0
    tiz = 0
    ot = 0
    ketto = 0
    egy = 0
    while osszeg != 0:
        while osszeg/1000 >=1:
            ezres+=1
            osszeg-=1000
        while osszeg/500 >=1:
            otszaz+=1
            osszeg-=500
        while osszeg/200 >=1:
            ketszaz+=1
            osszeg-=200
        while osszeg/100 >=1:
            szaz+=1
            osszeg-=100
        while osszeg/50 >=1:
            otven+=1
            osszeg-=50
        while osszeg/20 >=1:
            husz+=1
            osszeg-=20
        while osszeg/10 >=1:
            tiz+=1
            osszeg-=10
        while osszeg/5 >=1:
            ot+=1
            osszeg-=5
        while osszeg/2 >=1:
            ketto+=1
            osszeg-=2            
        while osszeg/1 >=1:
            egy+=1
            osszeg-=1
    if ezres != 0:
        print("Ezresek száma: ",ezres)
    if otszaz != 0:
        print("Ötszázasok száma: ",otszaz)
    if ketszaz != 0:
        print("Kétszázasok száma: ",ketszaz)
    if szaz != 0:
        print("Százasok száma: ",szaz)
    if otven != 0:
        print("Ötvenesek száma: ",otven)
    if husz != 0:
        print("Húszasok száma: ",husz)
    if tiz != 0:
        print("Tizesek száma: ",tiz)
    if ot != 0:
        print("Ötösök száma: ",ot)
    if ketto != 0:
        print("Kettesek száma: ",ketto)
    if egy != 0:
        print("Egyesek száma: ",egy)

def f10():
    f(10)
    elso =int(input("Adja meg az első elemet: "))
    diff =int(input("Adja meg a differenciát: "))
    elem =int(input("Adja meg az elemszámot: "))
    adat=elso
    print(elso)
    while elem != 0:
        print(adat+diff)
        adat+=diff
        elem-=1

def f11():
    f(11)
    n = int(input("Adja meg \"N\" pozitív egész számot.: "))
    szamlalo = 0
    osszeg = 0
    while szamlalo !=n+1:
        if szamlalo%2 == 1:
            osszeg+=szamlalo
            szamlalo+=1
        else:
            szamlalo+=1
    print(osszeg)

def f12():
    f(12)
    n = int(input("Adja meg \"N\" pozitív egész számot.: "))
    szamlalo = 1
    osszeg=1
    while szamlalo !=n+1:
        osszeg*=szamlalo
        szamlalo+=1
    print(osszeg)


    






def main():
    #f1()
    #f2()
    #f4()
    #f5()
    #f6()
    #f7()
    #f8()
    #f9()
    #f10()
    #f11()
    #f12()


main()