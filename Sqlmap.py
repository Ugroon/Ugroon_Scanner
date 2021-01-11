#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

os.system("figlet SQLMAP")
print("""

sqlmap aracına hoşgeldiniz.

1) Database adını öğrenme
2) Veri tabanına bağlı tabloları bulma
3) Tablolar içerisindeki kolonları görme
4) Dosyalar içerisindeki verileri alma

""")

secim = input("Seçim: ")

if secim == "1":
    secim1 = input("Hedef URL: ")

    os.system("sqlmap -u " + secim1 + " --level 5 --risk 3 --dbs")
    
    print(""" 
    """)

    a = input("Diğer aşamalara geçmek için sqlmap'i yeniden çalıştırmak istermisiniz? (E/h): ")

    os.system("clear")

    if a == "e":
        
        os.system("python3 Sqlmap.py")

    elif a == "E":
        
        os.system("python3 Sqlmap.py")

    else:

        exit()
    

elif secim == "2":

    secim2 = input("Hedef URL: ")

    secim21 = input("Veri tabanı ismi: ")

    os.system("sqlmap -u " + secim2 + " --level 5 --risk 3 -D " + secim21 + " --tables")
    
    print(""" 
    """)

    b = input("Diğer aşamalara geçmek için sqlmap'i yeniden çalıştırmak istermisiniz? (E/h): ")

    os.system("clear")

    if b == "e":
        
        os.system("python3 Sqlmap.py")

    elif b == "E":
        
        os.system("python3 Sqlmap.py")

    else:

        exit()
    

elif secim == "3":
    
    secim3 = input("Hedef URL: ")

    secim31 = input("Veri tabanı ismi: ")

    secim32 = input("Kolonları bulunacak tablo: ")

    os.system("sqlmap -u " + secim3 + " --level 5 --risk 3 -D " + secim31 + " -T " + secim32 + " --columns")

    print(""" 
    """)
    
    c = input("Diğer aşamalara geçmek için sqlmap'i yeniden çalıştırmak istermisiniz? (E/h): ")

    os.system("clear")

    if c == "e":
        
        os.system("python3 Sqlmap.py")

    elif c == "E":
        
        os.system("python3 Sqlmap.py")

    else:

        exit()
    
    
elif secim == "4":

    secim4 = input("Hedef URL: ")

    secim41 = input("Veri tabanı ismi: ")

    secim42 = input("Kolonları bulunacak tablo: ")

    secim43 = input("İçeriği görüntülenecek kolon: ") 

    os.system("sqlmap -u " + secim4 + " --level 5 --risk 3 -D " + secim41 + " -T " + secim42 + " -C" + secim43)

    print(""" 
    """)
    
    d = input("Diğer aşamalara geçmek için sqlmap'i yeniden çalıştırmak istermisiniz? (E/h): ")

    os.system("clear")
    
    if d == "e":
        
        os.system("python3 Sqlmap.py")

    elif d == "E":
        
        os.system("python3 Sqlmap.py")

    else:

        exit()
    

else:
    print("Hatalı giriş yapıldığı için program kapatıldı.")

    exit()
