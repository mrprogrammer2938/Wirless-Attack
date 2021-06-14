#!/usr/bin/python3
# This code write by Mr.nope
import os
import time
import platform
import sys
from core import wifi
class color:
	green = '\033[92m'
	red = '\033[91m'
	End = '\033[0m'
system = platform.uname()[0]
opt = "\nWirless-Attack ~# "
def cls():
	os.system("cls")
def start():
	title()
	cls()
	try_to_Attack()
def try_to_Attack():
	try1 = input("\nDo you want to start Attack? [y/n] ")
	if try1 == 'y':
		wifi.attack()
		try_to_continue()
	elif try1 == 'n':
		try_to_menu()
	else:
		try_to_Attack()
def ext():
	cls()
	print("\033[92mExiting...\033[0m")
	sys.exit()
def menu():
	title()
	cls()
	banner()
	list()
def try_to_continue():
	try2 = input("Do you want to try again? [y/n] ")
	if try2 == 'y':
		wifi.attack()
		try_to_continue()
	elif try2 == 'n':
		cls()
		try3()
	else:
		try_to_continue()
def list():
	print("\n{1}-Online Attack!")
	print("{2}-Installing Wirless Attack Tool!")
	print("{3}-Developer")
	print("{4}-Exit")
	choose = input(opt)
	if choose == '1':
		start()
	elif choose == '2':
		menu2()
	elif choose == '3':
		dev()
	elif choose == '4':
		ext()
	else:
		cls()
		print(choose + "\033[91m Not Found!\033[0m")
		try_to_menu()
def banner():
	print("""\033[92m
██     ██ ██ ██████  ██      ███████ ███████ ███████        █████  ████████ ████████  █████   ██████ ██   ██ 
██     ██ ██ ██   ██ ██      ██      ██      ██            ██   ██    ██       ██    ██   ██ ██      ██  ██  
██  █  ██ ██ ██████  ██      █████   ███████ ███████ █████ ███████    ██       ██    ███████ ██      █████   
██ ███ ██ ██ ██   ██ ██      ██           ██      ██       ██   ██    ██       ██    ██   ██ ██      ██  ██  
 ███ ███  ██ ██   ██ ███████ ███████ ███████ ███████       ██   ██    ██       ██    ██   ██  ██████ ██   ██ \033[0m""")

def menu2():
	cls()
	print("""\033[96m
 _       ___      __                     ___   __  __             __
| |     / (_)____/ /__  __________      /   | / /_/ /_____ ______/ /__
| | /| / / / ___/ / _ \/ ___/ ___/_____/ /| |/ __/ __/ __ `/ ___/ //_/
| |/ |/ / / /  / /  __(__  |__  )_____/ ___ / /_/ /_/ /_/ / /__/ ,<
|__/|__/_/_/  /_/\___/____/____/     /_/  |_\__/\__/\__,_/\___/_/|_|
\033[0m""")
	print("\n{1}-Wirless-attack")
	print("{2}-wifite")
	print("{3}-AirCrack-ng")
	print("{4}-wifiSpy")
	print("{5}-mein menu")
	choose2 = input(opt)
	if choose2 == '1':
		cls()
		os.system("git clone https://github.com/bitcoinander/wiresec")
		try6()
	elif choose2 == '2':
		cls()
		os.system("git clone https://github.com/derv82/wifite")
		try6()
	elif choose2 == '3':
	    cls()
	    os.system("git clone https://github.com/aircrack-ng/aircrack-ng")
	    try6()
	elif choose2 == '4':
		cls()
		os.system("git clone https://github.com/AresS31/wirespy")
		try6()
	elif choose2 == '5':
		menu()
	else:
		menu2()
def try_to_menu():
	try4 = input("\npress Enter...")
	if try4 == '':
		menu()
	else:
		menu()
def try6():
	try_to_menu2 = input("\npress Enter...")
	if try_to_menu2 == '':
		menu2()
	else:
		menu2()
def try8():
	try_to_exit = input("\npress Enter...")
	if try_to_exit == '':
		cls()
		print("\033[92mExiting...\033[0m")
		sys.exit()
	else:
		cls()
		print("\033[92mExiting...\033[0m")
		sys.exit()
def try10():
	try_to_4 = input("\npress Enter...")
	if try_to_4 == '':
		menu()
	else:
		menu()
def dev():
	cls()
	print("""\033[95m
 ____                 _
|  _ \  _____   _____| | ___  _ __   ___ _ __
| | | |/ _ \ \ / / _ \ |/ _ \| '_ \ / _ \ '__|
| |_| |  __/\ V /  __/ | (_) | |_) |  __/ |
|____/ \___| \_/ \___|_|\___/| .__/ \___|_|
                             |_|
\033[0m""")
	print("\n\033[91mThis code write by \033[92mMr.nope\033[0m")
	print("\n\033[33mVersion: \033[34m1.3.0\033[0m")
	print("\n\033[96mGithub: \033[4mhttps://github.com/mrprogrammer2938 \033[0m")
	time.sleep(2)
	try10()
def title():
	os.system("title Wirless-Attack")
def try3():
	try_to_3 = input("\nDo you want back to mein menu? [y/n] ")
	if try_to_3 == 'y':
		menu()
	elif try_to_3 == 'n':
		cls()
		try8()
	else:
		try3()
def try7():
	try_to_menu2_2 = input("\npress Enter...")
	if try_to_menu2_2 == '':
		menu2()
	else:
		menu2()
if __name__ == '__main__':
	try:
		if system == 'Linux':
			print("\nPlease, Run This Programm on Windows!\n")
			sys.exit()
		elif system == 'Mac':
			print("\nPlease, Run This Programm on Windows!\n")
			sys.exit()
		elif system == 'Windows':
			menu()
		else:
			print("\nPlease, Run This Programm on Windows!")
	except KeyboardInterrupt:
		print("\nCtrl + C")
		print("\nExiting...")
		sys.exit()