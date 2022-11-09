import os
from colorama import Fore
from colorama import Style


file = input("please enter your file's name: ")

Extension = file.split('.')[1]

print(f"file extension is:", Fore.RED + Extension + Style.RESET_ALL)
