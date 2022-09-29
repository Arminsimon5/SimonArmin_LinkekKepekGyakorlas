import math
from random import randint



def f1():
    print("\n\n1.feladat")
    for i in range(51):
        print(i)
    print("")

    for i in range(182,213):
        print(i)
    print("")

    for i in range(100,201,2):
        print(i)
    print("")

    for i in range(89,56,-2):
        print(i)
    print("")

    for i in range(1,21):
        print(i,"négyzete:",i*i)
    print("")

    for i in range(99,0,3):
        print(i)
    print("")

    for i in range(100,49,-5):
        print(i*2)
    print("")

    for i in range(1,1000):
        print(i,end=",")
    print("1000",end=".")
    print("")

    for i in range(1000,0,-3):
        print(i)

def f2():
    print("\n\n2.feladat")
    for i in range(0,100):
        print("*",end=" ")
    print("")
    szam=int(input("Adja meg hányszor adja meg a választott karaktert: "))
    karakter = (input("Adja meg a karaktert: "))
    for i in range(szam):
        print(karakter,end=" ")
    print("")
    szoveg = input("Adjon meg egy szöveget: ")
    for i in range(len(szoveg)+4):
        print("*",end="")
    print("")
    print("*",szoveg,"*")
    for i in range(len(szoveg)+4):
        print("*",end="")
    print("")
    for i in range(4):
        for i in range(4):
            print("*","",end="")
        print("")
        for i in range(4):
            print("","*",end="")
        print("")

def f3():
    print("\n\n3.feladat")
    szam1= int(input("Adjon meg egy egész számot: "))
    szam2= int(input("Adjon meg egy másik egész számot: "))
    lepeskoz = int(input("Adja meg a lépésközt: "))
    if szam1>szam2:
        for i in range(szam2,szam1,-lepeskoz):
            print(i)
    elif szam1<szam2:
        for i in range(szam1,szam2,lepeskoz):
            print(i)
        
def f4():
    print("\n\n4.feladat")
    n = int(input("Adja meg az \"n\"-t: "))
    for i in range(n):
        print(i*i,end=";")

def f5():
    print("\n\n5.feladat")
    n = int(input("Adja meg az \"n\"-t: "))
    for i in range(n):
        print(i*i*i)

def f6():
    print("\n\n6.feladat")
    a = int(input("Adjon meg egy számot: "))
    b = int(input("Adjon meg még egy számot: "))
    if(b>a):
        for i in range(a,b):
            print(round(math.sqrt(i),2))
    else:
        for i in range(b,a):
            print(round(math.sqrt(i),2))

def f7():
    print("\n\n7.feladat")
    n = int(input("Adja meg az \"n\"-t: "))
    faktorial=1
    for i in range(1,n+1):
        faktorial=faktorial*i
    print(faktorial)

def f8():
    print("\n\n8.feladat")
    n = int(input("Adja meg az \"n\"-t: "))
    for i in range(n):
        print(i*i)

def f9():
    print("\n\n9.feladat")
    n = int(input("Adja meg az \"N\"-t: "))
    osszeg=0
    for i in range(1,n+1,2):
        osszeg+=i
    print(osszeg)

def f10():
    print("\n\n10.feladat")
    k = int(input("Adja meg az \"K\" pozitív számot: "))
    osszeg=0
    for i in range(k+1):
        osszeg+=i*(i+1)
    print(osszeg)

def f11():
    print("\n\n11.feladat")
    n = int(input("Adja meg az \"N\" természetes számot: "))
    for i in range(0,n,3):
        print(i)

def f12():
    print("\n\n12.feladat")
    n = int(input("Adja meg az \"N\"-t: "))
    k=0
    j=1
    print(k,end=",")
    for i in range(1,n):
        h=k+j
        j=k
        k=h
        print(h,end=",")

def f13():
    print("\n\n13.feladat")
    n = int(input("Adja meg \"N\"-t: "))
    for i in range(1,n+1,1):
        k=0
        for j in range(1,n+1,1):
            if(i%j==0):
                k+=1
        if(k==2):
            print(i,end=", ")

def f14():
    print("\n\n14.feladat")
    print("*  1 2 3 4 5 6 7 8 9 10\n   --------------------")
    for i in range(1,11):
        print(i,"|",i*1,"",i*2,"",i*3,"",i*4,"",i*5,"",i*6,"",i*7,"",i*8,"",i*9,"",i*10)

def f15():
    print("\n\n15.feladat")
    print(randint(0,10))
    print(randint(0,25))
    print(randint(10,75))
    print(randint(-50,50))
    print(randint(-100,-70))

def f16():
     print("\n\n16.feladat")
     szam = int(input("Adjon meg egy számot: "))
     for i in range(szam):
        for j in range(szam):
            print("*",end="")
        print("")

def f17():
    print("\n\n17.feladat")    
    m = int(input("Adjon meg egy természetes számot: "))
    n = int(input("Adjon meg mégegy természetes számot: "))    
    for i in range(m):
        for j in range(n):
            print("*",end="")
        print("")    
            
def f18():
    print("\n\n18.feladat")
    n = int(input("Adjon meg egy természetes számot: "))
    m = int(input("Adjon meg mégegy természetes számot: "))    
    for i in range(n):
        for j in range(n-i):
            print(" ",end="")
        for k in range(m):
            print("*",end="")
        print("")

def f19():
    print("\n\n19.feladat")
    n = int(input("Adjon meg egy természetes számot: "))
    print("")
    m = 1
    for i in range(n):
        for j in range(n-i):
            print(" ",end="")
        for k in range(m):
            print("*",end="")
        m+=2
        print("")
    
def f20():
    print("\n\n20.feladat")
    m = int(input("Adjon meg egy természetes számot: "))
    n = int(input("Adjon meg mégegy természetes számot: "))
    for i in range(m):
        print("*",end="")
    print("")
    for j in range(n-2):
        print("*",end="")
        for k in range(m-2):
            print(" ",end="")
        print("*",end="")
        print("")
    for i in range(m):
        print("*",end="")

def f21():
    print("\n\n21.feladat")
    szam = int(input("Hány feladatot szeretne? "))
    for i in range(szam):
        a =randint(1,100)
        b =randint(1,100)
        print("A két szám: ",a,"és",b )
        osszeg = int(input("Mennyi összege: "))
        kulonb=int(input("Mennyi különbsége: "))
        if(osszeg ==a+b):
            print("A két szám összege valóban ennyi.")
        else:
            print("A két szám összege nem megfelelő")
        if(kulonb ==a-b):
            print("A két szám különbsége valóban ennyi.")
        else:
            print("A két szám különbsége nem megfelelő")

def f22():
    print("\n\n22.feladat")
    print("Kód  Karakter")
    for i in range(32,256):
        print(i," ",chr(i))

def f23():
    print("\n\n23.feladat")
    n = int(input("Adjon meg egy pozitív egész számot: "))
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end=(", "))

def f24():
    print("\n\n24.feladat")
    n = int(input("Adjon meg egy pozitív egész számot: "))
    osszeg=0
    for i in range(1,n+1):
        if(n%i==0):
            osszeg+=i
    print("Az osztóinak az összege: ",osszeg)

def f25():
    print("\n\n25.feladat")
    n = int(input("Adjon meg egy pozitív egész számot: "))
    osszeg=0
    for i in range(1,n+1):
        if(n%i==0):
            osszeg+=i
    if(osszeg==n*2):
        print("Ez egy tökéletes szám.")
    else:
        print("Ez nem egy tökéletes szám.")

def f26():
    print("\n\n26.feladat")
    szam1 = int(input("Adja meg a hatványalapot: "))
    szam2 = int(input("Adja meg a kitevőt: "))
    hatvanyertek=1
    for i in range(szam2):
        hatvanyertek=hatvanyertek * szam1
    print(hatvanyertek)

def f27():
    print("\n\n27.feladat")
    for j in range(26):
        for i in range(65+j,91):
            print(chr(i),end="")
        for i in range(65,65+j):
            print(chr(i),end="")
        print("")

def main():
    f1()
    f2()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()
    f9()
    f10()
    f11()
    f12()
    f13()
    f14()
    f15()
    f16()
    f17()
    f18()
    f19()
    f20()
    f21()
    f22()
    f23()
    f24()
    f25()
    f26()
    f27()


main()
