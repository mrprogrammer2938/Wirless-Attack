#!/usr/bin/python3
# This code write by Mr.nope
import os
import time
import subprocess
import sys
def cls():
	os.system("cls")
def attack():
	cls()
	wifi = subprocess.getoutput("netsh wlan show profile").replace("Profiles on interface Wi-Fi:","Wriless-Attack:").replace("Group policy profiles (read only)","Stating...").replace("---------------------------------","-==============================================-").replace("<None>","").replace("User profiles","All User:  |  Password:").replace("All User Profile","User").replace("    User","User").replace("-------------","---------------------------------")
	print(wifi)