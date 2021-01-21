#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


import time


os.system("clear")

os.system("apt install chkrootkit && apt full-upgrade chkrootkit")

os.system("clear")

os.system("figlet Rootkit Tarama")

time.sleep(3)

os.system("chkrootkit")

print("""


""")

restart = input("Rootkit aracını yeniden başlatmak istermisiniz? (E/h): ")

uppere = str("E")

if uppere == upper.restart():

    os.system("python3 Rootkit.py")

elif restart == "":

    os.system("python3 Rootkit.py")

else:

    exit()
