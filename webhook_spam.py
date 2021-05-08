import requests
import colorama
from colorama import Fore, Back, Style

#imported colorama just to make the code fancier

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



    main_stuff={'content':content,'username':username,'avatar_url':picture}
    while True:
        r= requests.post(web,data=main_stuff)     #does the execution part
        if r.status_code==204:
            print(f"{Fore.GREEN} >>>>>> Message Sent >>>>")
        else:
            print(f"{Fore.BLACK} >>>>>> Delay(please wait) >>>>>>")
    
main()



