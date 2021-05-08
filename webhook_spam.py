import requests
import colorama
from colorama import Fore, Back, Style
import os
#imported colorama just to make the code fancier

os.system('title webhook spammer~by Inferno')

Creator = f"""
Made by:
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█▄ ▄█ ▄▄▀█ ▄▄█ ▄▄█ ▄▄▀█ ▄▄▀█▀▄▄▀
██ ██ ██ █ ▄██ ▄▄█ ▀▀▄█ ██ █ ██ 
█▀ ▀█▄██▄█▄███▄▄▄█▄█▄▄█▄██▄██▄▄█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""

def main():
    print(Creator)
    web= input(f"{Fore.RED}Please enter the Webhook link here:")
    username = input(f"{Fore.BLUE}Webhook Name (ur choice):")
    picture = input(f"{Fore.BLUE}Webhook avatar (skip if you want none)?:")
    content = input(f"{Fore.RED}Message You want to spam:")



    main_stuff={'content':content   ,        'username':username       ,      'avatar_url':picture      }
    while True:
        r= requests.post(web,data=main_stuff)     #does the execution part
        print(f"{Fore.GREEN}  >>>>>> Message Sent >>>>")
    

main()



