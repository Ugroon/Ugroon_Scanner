#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

import time

os.system("apt install wafw00f && apt upgrade wafw00f")

os.system("clear")

os.system("figlet Guvenlik Duvari Tespit")

print("""
1) Bulunabilinen güvenlik duvarları

2) Güvenlik duvarı bulma


""")

secim = input("Seçenek: ")

if secim == "1":
    
    os.system("wafw00f -l")
    
    
elif secim == "2":
    
    print("""

Güvenlik duvarı tespit programına hoş geldiniz.

""")

    hedef = input("Hedef site: ")

    os.system("clear")

    os.system("wafw00f " + hedef)

    tekrar = input("Programı tekrar başlatmak istermisiniz? (E/h): ")

    e = str("E")

    if e == tekrar.upper():

        os.system("python3 wafw00f.py")
    
    elif tekrar == "":
    
        os.system("python3 wafw00f.py")

    else:

        exit()
        
else:
    
    print("Hatalı seçim yaptığınız için program kapatılıyor...")
    
    time.sleep(3)
    
    exit()
    
