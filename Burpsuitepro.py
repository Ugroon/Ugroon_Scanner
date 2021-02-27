#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

import os

os.system("clear")

os.system("figlet Burp Suite PRO")

time.sleep(3)

os.system("/usr/lib/jvm/java-11-openjdk-amd64/bin/java --illegal-access=permit -Dfile.encoding=utf-8 -javaagent:BurpSuiteLoader_v2020.12.1.jar -noverify -jar burpsuite_pro_v2020.12.1.jar")

