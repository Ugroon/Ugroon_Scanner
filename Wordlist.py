#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

os.system("clear")

os.system("apt -y install crunch")

os.system("apt -y full-upgrade crunch")

os.system("clear")

os.system("figlet Wordlist Olusturma")

print("""


Wordlist oluşturma aracına hoşgeldiniz


""")

minimum = input("Kullanılacak minimum karakter sayısı: ")

print("""

""")

maksimum = input("Kullanılacak maksimum karakter sayısı: ")

print("""

""")

harfler = input("Kullanılacak karakterler: ")

print("""

""")

konum = input("Wordlist'in kaydedileceği dosya konumu: ")

os.system("crunch " + minimum + " " + maksimum + " " + harfler + " -O " + konum )

word = input("Yeni wordlist oluşturmak istermisiniz? (E/h): ")

worde = "E"

if word == "":

    os.system("python3 Wordlist.py")

    exit()

elif worde == word.upper():

    os.system("python3 Wordlist.py")

    exit()


else:

    exit()
