import os 
import time 
import sys 

title = '* Title : [PROGRAM RUSAK HP]'
Name = "* Author : [XLINUX]"
yt = "* Youtube  : [x linux]"
print()
print(title)
time.sleep(0.20)
print(Name)
time.sleep(0.20)
print(yt)
time.sleep(0.20)

def play():
    x ="""
[1] +62
[2] 08
[0] Exit"""
    print(x)
    print()
    pilih =input("Pilih ( 1/ 2 / 0) :")
    if pilih.lower() == "1":
        ans =input("Masukan Nomor Target (+62) :")
        os.system("clear")
        print(title)
        time.sleep(0.20)
        print(Name)
        time.sleep(0.20)
        print(yt)
        time.sleep(0.20)
        print()
        while ans == ans:
            print(ans,"Sedang Di Attack !!!!!")
            time.sleep(0.10)
    
    elif pilih.lower() == "2":
        ani =input("Masukan Nomor Target (08) :")
        os.system("clear")
        print(title)
        time.sleep(0.20)
        print(Name)
        time.sleep(0.20)
        print(yt)
        time.sleep(0.20)
        print()
        while ani == ani:
            print(ani,"Sedang Di Attack !!!!!")
            time.sleep(0.10)
  
    else:
        if pilih.lower() == "0":
            os.system("clear")
            sys.exit("LOL!")
        




play()






    



