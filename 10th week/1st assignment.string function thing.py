import math
import os
from colorama import Fore
from colorama import Style


def delta(a, b, c):
    d = (((b) ** (2)) - ((4) * (a) * (c)))
    return d


os.system("cls")
a = int(input(f"enter {Fore.RED}a{Style.RESET_ALL}: "))
b = int(input(f"enter {Fore.RED}b{Style.RESET_ALL}: "))
c = int(input(f"enter {Fore.RED}c{Style.RESET_ALL}: "))

d = delta(a, b, c)

if d < 0:
    print(f"there is no ans for '{Fore.RED}x{Style.RESET_ALL}'")

elif d == 0:
    x = (((-1) * (b)) / ((2) * (a)))
    print(f"there is one ans for '{Fore.RED}x{Style.RESET_ALL}' and it's: ", Fore.GREEN + str(x) + Style.RESET_ALL)

elif d > 0:
    x1 = ((((-1) * (b)) + (math.sqrt(d))) / ((2) * (a)))
    x2 = ((((-1) * (b)) - (math.sqrt(d))) / ((2) * (a)))
    print(f"'{Fore.RED}x1{Style.RESET_ALL}' is: ", Fore.GREEN + str(x1) + Style.RESET_ALL)
    print(f"'{Fore.RED}x2{Style.RESET_ALL}' is: ", Fore.GREEN + str(x2) + Style.RESET_ALL)
