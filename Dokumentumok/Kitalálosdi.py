import random
import sys
import os
import subprocess
import time
print("Gondoltam egy számra 1 és 1000 között. Találd ki ezt a számot.")
bekért = int(input("Adjon meg egy számot 1-1000 között: "))
randomSzám = random.randint(1,1000)
while(randomSzám != bekért):
    if(bekért > 0):
        if(bekért < 1001):
            if(bekért > randomSzám):
                print("Kisebb számra gondoltam. :P")
                bekért = int(input("Adjon meg egy másik számot."))
            if(bekért < randomSzám):
                print("Nagyobb számra gondoltam. :D")
                bekért = int(input("Adjon meg egy másik számot."))
        else:
            print("Hülye maga?? :D Kisebb számot adjon meg. ")
            bekért = int(input("Adjon meg egy másik számot."))
    else:
        print("Hülye maga?? :D Nagyobb számot adjon meg. ")
        bekért = int(input("Adjon meg egy másik számot."))

    if(randomSzám == bekért):
        print("Ügyes erre a számra gondoltam:", randomSzám)
        bekért2 = input("Szeretné újrakezdeni? \"Y\" vagy \"N\"")
        while(bekért2 !='N' or 'Y'):
            if(bekért2 == 'Y'):
                subprocess.call([sys.executable, os.path.realpath("Kitalálosdi.py")] + sys.argv[1:])
            elif(bekért2 == 'N'):
                print("Viszlát késöbb!")
                print("#####        #####")
                print("#####        #####")
                print("#####        #####")
                print("\n  ##          ##  ")
                print("   ##       ##")
                print("     #######")
                time.sleep(2)
                sys.exit()
            else:
                print("Nem értelmezhető!")
"""        
        if(bekért2 == 'Y'):
            subprocess.call([sys.executable, os.path.realpath("Kitalálosdi.py")] + sys.argv[1:])
        if(bekért2 == 'N'):
            print("Viszlát késöbb!")
            print("#####        #####")
            print("#####        #####")
            print("#####        #####")
            print("\n  ##          ##  ")
            print("   ##       ##")
            print("     #######")
            time.sleep(2)
            sys.exit()
"""