import os
import numpy as np
from colorama import Fore
from colorama import Style

os.system("cls")
size_y = int(input(f"please enter {Fore.RED}x{Style.RESET_ALL} ratio: "))
size_x = int(input(f"please enter {Fore.RED}y{Style.RESET_ALL} ratio: "))


x = np.zeros((size_x, size_y), dtype = str)

x[1::2, ::2] = "&"
x[::2, 1::2] = "$"

for i in range(size_x):
    for j in range(size_y):
        print(x[i][j], end=" ")
    print()