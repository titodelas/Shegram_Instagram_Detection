import instaloader
import time
import os
import requests
import webbrowser

import fade
from colorama import Fore, init, Style
init(autoreset=True)
v = '2.1'
L = instaloader.Instaloader()

banner = fade.fire('''
 .d8888b.  888    888 Y88b   d88P  .d8888b.  8888888b.         d8888 888b     d888 
d88P  Y88b 888    888  Y88b d88P  d88P  Y88b 888   Y88b       d88888 8888b   d8888 
Y88b.      888    888   Y88o88P   888    888 888    888      d88P888 88888b.d88888 
 "Y888b.   8888888888    Y888P    888        888   d88P     d88P 888 888Y88888P888 
    "Y88b. 888    888     888     888  88888 8888888P"     d88P  888 888 Y888P 888 
      "888 888    888     888     888    888 888 T88b     d88P   888 888  Y8P  888 
Y88b  d88P 888    888     888     Y88b  d88P 888  T88b   d8888888888 888   "   888 
 "Y8888P"  888    888     888      "Y8888P88 888   T88b d88P     888 888       888 
                                                                                   ''')

def photo():
    global path
    global username
    bot = instaloader.Instaloader()
    path = os.getcwd()  # Obtain the actual directory path
    username = input(f"Instert Instagram account: {Fore.CYAN}@")
    print(Fore.RESET)
    print(bot.download_profile(username, profile_pic_only=True))

def detect_file():  # Trying to detect the .jpg file
    global file
    time.sleep(1)  # Whait time to create the folder with the pfp

    for file in os.listdir(f"{path}/{username}"):
        if file.endswith(".jpg"):  # Instagram pfp save as .jpg
            # Rename the file to make easy the detection
            os.rename(f'{path}/{username}/{file}',
                      f'{path}/{username}/{username}.jpg')
        else:
            pass

def reverse_lookup():  # Upload photo to Google Image Search
    filePath = f'{path}/{username}/{username}.jpg'
    searchUrl = 'http://www.google.hr/searchbyimage/upload'
    multipart = {'encoded_image': (filePath, open(
        filePath, 'rb')), 'image_content': ''}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']
    webbrowser.open(fetchUrl)

def database():
    save = input(f'Do you want to add {Fore.CYAN}@{username}{Fore.RESET} to SheGram Database? (y/n): ')
    ID = instaloader.Profile.from_username(L.context, username)
    if (save == 'y'):
        with open(f"{path}/database.txt", "a") as f:
            f.write(f'''
USERNAME: {username}
ACCOUNT ID: {ID}
====================''')
    if (save == 'n'):
        print('Thanks for using SheGram :)')
        quit()

def id_finder():
    account = input(f'Input the account name: {Fore.CYAN}@')
    print(Fore.RESET)
    profile = instaloader.Profile.from_username(L.context, account)
    print(f"The ID for {Fore.CYAN}{account}{Fore.RESET} is: {profile.userid}")

def username_finder():
    ID = input('Input the account id: ')
    profile = instaloader.Profile.from_id(L.context, ID)
    print(f"The Account related with the ID {Fore.CYAN}{ID}{Fore.RESET} is: {profile.username}")

def menu():
    os.system('cls')
    print(banner)
    print(f'''                       {Fore.YELLOW}She{Fore.RESET}rlock Insta{Fore.YELLOW}gram{Fore.RESET} Tool
    {Fore.RED}╔════════════════════════════╗╔═══════════════════════════════╗
    {Fore.RED}║{Fore.RESET} [{Fore.CYAN}1{Fore.RESET}] Fake Account Checker   {Fore.RED}║║{Fore.RESET} [{Fore.GREEN}</>{Fore.RESET}] Build By Edu Olivares   {Fore.RED}║
    {Fore.RED}║{Fore.RESET} [{Fore.CYAN}2{Fore.RESET}] Check SHYGRAM Database {Fore.RED}║║{Fore.RESET} [{Fore.BLUE}-?-{Fore.RESET}] This is the {v} version {Fore.RED}║
    {Fore.RED}║{Fore.RESET} [{Fore.CYAN}3{Fore.RESET}] Find Username With ID  {Fore.RED}║║{Fore.RESET} [{Fore.YELLOW}-!-{Fore.RESET}] Unther the GPL Licence  {Fore.RED}║
    {Fore.RED}║{Fore.RESET} [{Fore.CYAN}4{Fore.RESET}] Find ID With Username  {Fore.RED}║║{Fore.RESET} [{Fore.CYAN}_*_{Fore.RESET}] Made In Spain           {Fore.RED}║
    {Fore.RED}╚════════════════════════════╝╚═══════════════════════════════╝
    ''')
    global option
    option = input(f'Choose a Tool {Fore.YELLOW}>{Fore.CYAN}>{Fore.GREEN}>{Fore.RESET} ')
    if (option == "1"):
        os.system('cls')
        print(banner)
        photo()
        detect_file()
        reverse_lookup()
        database()
    if (option == "2"):
        os.system('cls')
        print('In Development...')
        menu()
    if (option == "3"):
        os.system('cls')
        print(banner)
        username_finder()
    if (option == "4"):
        os.system('cls')
        print(banner)
        id_finder()


menu()