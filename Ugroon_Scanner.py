#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

os.system("apt update")
os.system("apt full-upgrade")
os.system("apt install figlet")
os.system("apt full-upgrade figlet")
os.system("apt install git")
os.system("apt full-upgrade git")
os.system("clear")
os.system("figlet WELCOME TO UGROON SCANNER")

print("""
1) Nmap
2) Zaproxy
3) Skipfish
4) XSpear
5) Nikto
6) Searchsploit
7) Nmap , Uniscan , Golismero , Wafw00f , SSLyze , Fierce , LBD , DNSRecon , Theharvester ve diğer araçların toplu şekilde bulunduğu tarama programı

""")
secim = input("Seçenek: ")
os.system("clear")
if secim == "1":
    print("""

1) Hızlı tarama
2) Versiyon bilgisi
3) İşletim sistemi bilgisi
4) İp adresine bağlı diğer ip adresleri
5) E-host keşfinden sonra tarama
6) DNS çözümlemesi olmadan tarama
7) DNS çözümlemesi ile tarama

""")
    secenek = input("Seçenek: ")

    ip = input("Hedef ip adresi: ")
    os.system("clear")

    if secenek == "1":
        os.system("nmap " + ip)

    elif secenek == "2":
        os.system("nmap -sS -sV " + ip)

    elif secenek == "3":
        os.system("nmap  -O " + ip)

    elif secenek == "4":
        os.system("nmap -sL " + ip)

    elif secenek == "5":
        os.system("nmap -sn " + ip)

    elif secenek == "6":
        os.system("nmap -n " + ip)

    elif secenek == "7":
        os.system("nmap -R " + ip)

    else:
        print("Böyle bir seçenek yok! Program kapatılıyor.")
        import time
        time.sleep(3)
        exit()
    
        
    restart = input("Programı yeniden başlatmak istermisiniz? (E/h): ")   
    
    if restart == "E":
        os.system("python3 Ugroon_Scanner.py")
        
    elif restart == "e":
        os.system("python3 Ugroon_Scanner.py")

    else:
        print("Program kapatıldı.")

        exit()

elif secim == "2":
    os.system("apt install zaproxy")
    os.system("apt full-upgrade zaproxy")
    os.system("zaproxy")
    os.system("clear")

elif secim == "3":
    os.system("apt install skipfish")
    os.system("apt-full-upgrade skipfish")
    skipfish = input("Taranacak site adresi(https:// ya da http:// ile): ")
    skipfish_sonuc = input("Tarama sonucunun kaydedileceği dizin: ")
    os.system("skipfish -o " + skipfish_sonuc + skipfish)
    print("Dosya kaydedildi")
    import time
    time.sleep(3)
    exit()
    
elif secim == "4":
    print("""
Not: Dosya bulunduğunuz dizine indirilecektir.

""")
    os.system("git clone https://github.com/hahwul/XSpear.git")
    os.system("cd XSpear")
    os.system("gem install XSpear")
    parametre = input("Parametre(Örneğin -v 2): ")
    xspear_site = input("Taranacak URL: ")
    os.system("XSpear " + parametre + xspear_site )
    
    
    
    restart = input("Programı yeniden başlatmak istermisiniz? (E/h): ")   
    
    if restart == "E":
        os.system("python3 Ugroon_Scanner.py")    
        
    elif restart == "e":
        os.system("python3 Ugroon_Scanner.py")

    else:
        print("Program kapatıldı.")

        exit()

elif secim == "5":
    os.system("sudo apt-get install nikto")
    os.system("sudo apt full-upgrade nikto")
    os.system("nikto update")
    os.system("clear")
    os.system("figlet Nikto")
    print("""

1) Bilgilendirme tarama modu
2) XSS ve javascript enjeksiyonu taraması
3) Hizmet reddi taraması
4) SQL enjeksiyon taraması
5) Normal Tarama

""")

    nikto_secim = input("Seçenek: ")
    print("""

""")

    hedefip = input("Taranacak ip adresi: ")
    os.system("clear")
    
    if nikto_secim == "1":
        os.system("nikto -Tuning 3 -h " + hedefip)
        
    elif nikto_secim == "2":
        os.system("nikto -Tuning 4 -h " + hedefip)
        
    elif nikto_secim == "3":
        os.system("nikto -Tuning 6 -h " + hedefip)
        
    elif nikto_secim == "4":
        os.system("nikto -Tuning 9 -h " + hedefip)
        
    elif nikto_secim == "5":
        os.system("nikto -h " + hedefip)

    else:
        print("Hatalı işlem yaptınız bu nedenle program kaptılıyor.")
        import time
        time.sleep(3)
        exit()
    
        
    restart = input("Programı yeniden başlatmak istermisiniz? (E/h): ")   
    
    if restart == "E":
        os.system("python3 Ugroon_Scanner.py")
        
    elif restart == "e":
        os.system("python3 Ugroon_Scanner.py")

    else:
        print("Program kapatıldı.")

        exit()   
        
elif secim == "7":

    os.system("git clone https://github.com/skavngr/rapidscan.git")
    os.system("cd rapidscan")

    os.system("figlet Rapidscan")
    print("""
    
    """)
    rapid_secim = input("Taranacak site adresi: ")

    os.system("clear")
    os.system("cd rapidscan && python rapidscan.py " + rapid_secim)
    
    restart = input("Programı yeniden başlatmak istermisiniz? (E/h): ") 
    
    if restart == "E":
        os.system("python3 Ugroon_Scanner.py")
        
    elif restart == "e":
        os.system("python3 Ugroon_Scanner.py")

    else:
        print("Program kapatıldı.")

        exit()

elif secim == "6":
    os.system("python3 Searchsploit.py")
    
    exit()
    
else:
    print("Hatalı işlem yaptınız bu nedenle program kapatılıyor.")
    import time
    time.sleep(3)
    exit()
