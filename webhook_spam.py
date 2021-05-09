import requests
import colorama
import asyncio
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
    web= input(f"{Fore.RED}Please enter the Webhook link here(Important) :")
    username = input(f"{Fore.BLUE}Webhook Name (Skip if you want none) :")
    picture = input(f"{Fore.BLUE}Webhook avatar (skip if you want none)? :")
    content = input(f"{Fore.RED}Message You want to spam(Important) :")
    l = input(f"{Fore.GREEN}Launch attack or restart (launch/restart)? :")
    if l=="launch":
        main_stuff={'content':content,'username':username,'avatar_url':picture}
        while True:
            r= requests.post(web,data=main_stuff) 
            if r.status_code==204:
                print(f"{Fore.GREEN} >>>>>> Message Sent >>>>")
            else:
                print(f"{Fore.BLACK} >>>>>> Delay(please wait) >>>>>>")

    elif l=="restart":
         main()
    else:
        print(f"{Fore.RED}===========================================")
        print(f"{Fore.YELLOW} ⚠Please enter a correct option! ")
        print(f"{Fore.RED}===========================================")
        pff = input(f"{Fore.GREEN} Restart (y/n)? : ")
        if pff == "y":
            main()
        else:
            exit()
            


    
    
main()


