#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

os.system("apt install wafw00f && apt upgrade wafw00f")

os.system("clear")

os.system("figlet Güvenlik Duvarı Tespit")

print("""

Güvenlik duvarı tespit programına hoş geldiniz.

""")

hedef = input("Hedef site: ")

os.system("wafw00f " + hedef)

tekrar = input("Programı tekrar başlatmak istermisiniz? (E/h): ")

e = str("E")

if e == tekrar.upper():

    os.system("python3 wafw00f.py")
    
elif tekrar == "":
    
    os.system("python3 wafw00f.py")

else:

    exit()
