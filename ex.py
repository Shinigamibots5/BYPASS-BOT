import os
from colorama import Fore, init
from requests import post

init(convert=True)

os.system('cls && title AIO BYPASS' if os.name == 'nt' else 'clear')

ascii = """

██████╗░██╗░░░██╗██████╗░██╗░░░██╗  ██████╗░██╗░░░██╗██████╗░░█████╗░░██████╗░██████╗  ██████╗░░█████╗░████████╗
██╔══██╗██║░░░██║██╔══██╗██║░░░██║  ██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║██║░░░██║██║░░██║██║░░░██║  ██████╦╝░╚████╔╝░██████╔╝███████║╚█████╗░╚█████╗░  ██████╦╝██║░░██║░░░██║░░░
██║░░██║██║░░░██║██║░░██║██║░░░██║  ██╔══██╗░░╚██╔╝░░██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗  ██╔══██╗██║░░██║░░░██║░░░
██████╔╝╚██████╔╝██████╔╝╚██████╔╝  ██████╦╝░░░██║░░░██║░░░░░██║░░██║██████╔╝██████╔╝  ██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚═════╝░╚═════╝░░╚═════╝░  ╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░
"""

def bp(link):
  data = {
    "url": link,
  }

  r = post("https://api.bypass.vip/", data=data)
  return r.json()

print(ascii.replace('$', Fore.RED+"$"+Fore.RESET))
print("")
link = open('1.txt', 'r').read()
b = bp(link)

if b['success'] == True:
    print(f"[{Fore.GREEN}+{Fore.RESET}] Website Found: {Fore.BLUE}{b['website']}{Fore.RESET}")
    print(f"{b['destination']}" ,file=open("2.txt", "w"))
    print(f"[{Fore.GREEN}+{Fore.RESET}] Bypassed In: {Fore.BLUE}{b['time_ms']}ms{Fore.RESET}")
else:
    print(f"[{Fore.RED}-{Fore.RESET}] An error has occured or this link is invalid !" ,file=open("2.txt", "w"))
