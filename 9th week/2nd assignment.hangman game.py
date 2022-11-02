import random
import os
from pyfiglet import Figlet
from colorama import Fore
from colorama import Style


f = Figlet(font='standard')
counter = 0
counter1 = 0
flag = None
guess_list = []
swear_names = ['shit' , 'fuck' , 'asshole' , 'fuckknuckels' , 'mfucker' , 'dick' , 'dickhead']
colors = ['yellow' , 'blue' , 'red' , 'black' , 'green' , 'white' , 'orange' , 'purple']
body_parts = ['penis' , 'breats' , 'ass' , 'vagina']
character_list = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']
c_character_list = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']


while True:
    os.system("cls")
    print(f"{Fore.RED}a.{Style.RESET_ALL} swears")
    print(f"{Fore.RED}b.{Style.RESET_ALL} colors")
    print(f"{Fore.RED}c.{Style.RESET_ALL} body parts")
    
    
    if flag == True:
        print(F"\n{Fore.RED}YOU IDIOT PIECE OF SHIT CHOOSE ONE OF THE {Fore.GREEN}OPTIONS{Fore.RED}!!!!!!!{Style.RESET_ALL}")
    chosen_list = input("\nplease choose one of the list above: ")
    if chosen_list == "a": 
        x = random.choice(swear_names)
        flag = None
        break
    elif chosen_list == "b":
        x = random.choice(colors)
        flag = None
        break
    elif chosen_list == "c":
        x = random.choice(body_parts)
        flag = None
        break
    else:
        flag = True
        continue
    

life_bar = len(x) + 1
for i in range(len(x)):
    guess_list.append('_')


while life_bar > 0 :
    os.system('cls')
    print()
    print(life_bar * f'{Fore.RED}❤ {Style.RESET_ALL}')
    print()
    print(character_list)
    
    
    if ((counter1 == len(character_list)) and (flag == False)) :
        print(f"{Fore.RED}\nPLEASE DON'T ENTER A PERVIOSLY USED CHARACTER!\n{Style.RESET_ALL}")
    if flag == True:
        print(f"{Fore.RED}\nPLEASE DON'T ENTER A PERVIOSLY USED CHARACTER IN CAPS!\n{Style.RESET_ALL}")
    for i in range(len(x)):
        print(guess_list[i] , end = ' ' )
    print('\n')
    
    
    counter = 0
    counter1 = 0
    flag = None    
    
    
    guessed_character = input(f'guess a character you {Fore.RED}PIECE OF SHIT{Style.RESET_ALL}: ')
    
    
    
    for i in range(len(character_list)):
        if (not(guessed_character == character_list[i])):
            counter1 += 1
            flag = False
    for i in range(len(c_character_list)):
        if guessed_character == c_character_list[i]:
            flag = True
    for i in range(len(character_list)):    
        if guessed_character == character_list[i]:
            character_list[i] = '_'
            continue
    for i in range(len(x)):
        if guessed_character == x[i]:
            guess_list[i] = guessed_character
            counter += 1
    
    
    if counter == 0:
        life_bar -= 1
    counter = 0
    for i in guess_list:
        if i == '_':
            counter += 1
    
    
    if counter == 0:
        os.system('cls')
        print("\nthe word is: \n\n\n" , Fore.GREEN + (f.renderText(x)) + Style.RESET_ALL)
        print(f"{Fore.GREEN}\nyou've won\n{Style.RESET_ALL}")
        break
for i in range(len(guess_list)):
    if guess_list[i] == '_':
        os.system('cls')
        print("\nthe word is: \n\n\n" , Fore.GREEN + (f.renderText(x)) + Style.RESET_ALL)
        print(f"{Fore.RED}\nyou've lost\n{Style.RESET_ALL}")
        break    