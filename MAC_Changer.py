#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

os.system("clear")

os.system("apt install macchanger && apt upgrade macchanger")

os.system("clear")

os.system("figlet MAC Adresi Degistirme")

print("""

MAC Adresi değiştirme programına hoş geldiniz.

1) MAC adresini rastgele değiştir

2) MAC adresini manuel olarak değiştir

3) MAC adresini orijinal haline çevir


""")

secim = input("Seçenek: ")


ag_karti = input("Sistem ağ kartı(ifconfig komutuyla çıkan ilk satır Örneğin eth0 ): ")

os.system("clear")

if secim == "1":

    os.system("clear")

    os.system("ifconfig " + ag_karti + " down")

    os.system("macchanger -r " + ag_karti)

    os.system("ifconfig " + ag_karti + " up")

    print("MAC Adresi Değiştirildi")

elif secim == "2":

    secim2 = input("Yeni MAC Adresi: ")

    os.system("ifconfig " + ag_karti + " down")

    os.system("macchanger --mac " + secim2 + " " + ag_karti)

    os.system("ifconfig " + ag_karti + " up")

    print("MAC Adresi Değiştirildi")

elif secim == "3":

    os.system("ifconfig " + ag_karti + " down")

    os.system("macchanger -p " + ag_karti)

    os.system("ifconfig " + ag_karti + " up")

    print("MAC Adresi Orijinal Haline Getirildi")

else:

    os.system("python3 MAC_Changer.py")

    

