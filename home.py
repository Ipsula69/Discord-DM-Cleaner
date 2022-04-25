import requests, os, sys, time, random, os.path, string, subprocess, pyperclip, pyautogui, urllib.request, random, threading, ctypes, base64, discord, json, datetime, shutil, aiohttp, asyncio
from colorama import Fore, init
from dhooks import Webhook
from tkinter import *
import tkinter.font as font
from selenium import webdriver
from PIL import Image
from itertools import cycle
from bs4 import BeautifulSoup
import requests as req
from threading import Thread as thr
from discord.ext import commands
from discord.ext.commands import Bot
from plyer import notification
from datetime import datetime
from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX

if os.name == "nt":
    os.system(f'title')

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{w}{b}{w}{w}... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

def discserver():
    print(f"""""")

def hometitle():
    discserver()
def cleardmtitle():
    discserver()                                                                                                   

def transition():
    os.system('cls' if os.name == 'nt' else 'clear')
    Spinner()
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    hometitle()
    print(f"""
\n   {w}Write [{b}1{w}] for cleaner
\n""")
    global choice
    choice = input(f"""\n: """)

    if choice == '1' or choice == '01':
        transition()
        exec(open('ac.py').read())

        if choice == '24':
            transition()
            sys.exit()  
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        main()

main()