import os
import colorama
import pyfiglet
import random
from colorama import Style
from pyfiglet import Figlet
from colorama import Fore
f = Figlet(font='standard')



def triangle_list(n):
    triangle = [[None for i in range(n)] for j in range(n)]
    return triangle

def triangle_boarders():     
    triangle = triangle_list(n)
    for i in range(n):
        triangle[i][0] = 1
        triangle[i][i] = 1
    return triangle

def triangle_mid():
    triangle = triangle_boarders()
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = (triangle[i-1][j] + triangle[i-1][j-1])
    return triangle

def print_triangle():
    triangle = triangle_mid()
    for i in range(n):
        for j in range(i + 1):
            print(Fore.RED + str(triangle[i][j]), end="\t")
        print()



while True:
    os.system("cls")
    title = "Pascal's triangle"
    print(Fore.GREEN + (f.renderText(title)) + Style.RESET_ALL)
    print("\n")
    jack = input(f"press {Fore.GREEN}enter{Style.RESET_ALL} to continue press {Fore.GREEN}'q'{Style.RESET_ALL} to quit! ")
    if jack == "":
        os.system("cls")
        n = int(input(f"Please enter the {Fore.GREEN}hight{Style.RESET_ALL} of the triangle: "))
        os.system("cls")
        triangle_list(n)
        triangle_boarders()
        triangle_mid()
        print_triangle()
        jack = input("")
        if jack == "\n":
            continue
    elif jack == "q":
        break
    else:
        continue
