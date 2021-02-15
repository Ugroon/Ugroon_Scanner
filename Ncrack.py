#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

os.system("clear")
os.system("apt install -y ncrack && apt full-upgrade -y ncrack")
os.system("clear")
os.system("figlet NCRACK")

print("""

Ncrack aracına hoş geldiniz

""")


ip = input("Hedef ip adresi: ")


port = input("Port numarası: ")


kullanici = input("Kaba kuvvet için kullanıcı adlarının bulunduğu dosya yolu: ")


sifre = input("Kaba kuvvet için parolaların bulunduğu dosya yolu: ")


os.system("ncrack -p " + port + " -U " + kullanici + " -P " + sifre + " " + ip)


print("""


      """)


restart = input("Programı yeniden başlatmak istermisiniz? (E/h): ")

e = str("E")


if e == restart.upper():

    os.system("python3 Ncrack.py")

elif restart == "":

    os.system("python3 Ncrack.py")

else:

    exit()
