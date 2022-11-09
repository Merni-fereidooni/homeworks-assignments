import os
from colorama import Fore
from colorama import Style

def word_counter(string):
    string.strip()
    word_count = print("the enterd statement has ",Fore.RED + str(len(string.split())) + Style.RESET_ALL, " words!")
    return word_count

os.system("cls")
statement = input("please enter a statement: ")
word_counter(statement)
