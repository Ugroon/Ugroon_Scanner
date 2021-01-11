#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

os.system("apt update")
os.system("apt full-upgrade")
os.system("apt install figlet")
os.system("apt full upgrade figlet")
os.system("apt install searchsploit")
os.system("apt full-upgrade searchsploit")
os.system("clear")
os.system("figlet WELCOME TO SEARCHSPLOİT")

print("""

Searchsploit aracına hoşgeldiniz.

""")


aranan = input("Aranacak exploit: ")

os.system("searchsploit " + aranan)

soru = input("Yeni arama yapmak istermisiniz? (e/h): ")

if soru == "E":
    os.system("python3 Searchsploit.py")
    
elif soru == "e":
    os.system("python3 Searchsploit.py")

else:
    print("Programdan çıkılıyor.")

    exit()
    
