import os
import colorama
import pyfiglet
from colorama import Style
from pyfiglet import Figlet
from colorama import Fore
f = Figlet(font='standard')



def create_board():
    list_2d = [['_', '_', '_'], 
               ['_', '_', '_'], 
               ['_', '_', '_']]
    return list_2d

def show_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

def condition_check(board, row, col):
    flag = False
    if ((0 <= row <= 2) and (0 <= col <= 2)):
        if (board[row][col] == "_"):
            flag = True
        else:
            print("this box is FULL")
    else:
        print("please enter valid row and column!")
    return flag

def user_input(board, sign):
    while True:
        row = int(input(f"\n\n[{Fore.RED}+{Style.RESET_ALL}] please enter {Fore.RED}row{Style.RESET_ALL}: ")) - 1
        col = int(input(f"[{Fore.RED}+{Style.RESET_ALL}] please enter {Fore.RED}column{Style.RESET_ALL}: ")) - 1

        if condition_check(board, row, col):
            board[row][col] = sign
            break
    return board

def row_check(board):
    flag1 = "r"
    #first row check
    if ((board[0][0] == "X") and (board[0][1] == "X") and (board[0][2] == "X")):
        flag1 = "s"
    elif ((board[0][0] == "O") and (board[0][1] == "O") and (board[0][2] == "O")):
        flag1 = "d"        
    #second row check
    elif ((board[1][0] == "X") and (board[1][1] == "X") and (board[1][2] == "X")):
        flag1 = "s"
    elif ((board[1][0] == "O") and (board[1][1] == "O") and (board[1][2] == "O")):
        flag1 = "d"
    #third row check
    elif ((board[2][0] == "X") and (board[2][1] == "X") and (board[2][2] == "X")):
        flag1 = "s"
    elif ((board[2][0] == "O") and (board[2][1] == "O") and (board[2][2] == "O")):
        flag1 = "d"
    return flag1

def col_check(board):
    #first row check
    flag2 = "r"
    if ((board[0][0] == "X") and (board[1][0] == "X") and (board[2][0]) == "X"):
        flag2 = "s"
    elif ((board[0][0] == "O") and (board[1][0] == "O") and (board[2][0] == "O")):
        flag2 = "d"        
    #second row check
    elif ((board[0][1] == "X") and (board[1][1] == "X") and (board[2][1] == "X")):
        flag2 = "s"
    elif ((board[0][1] == "O") and (board[1][1] == "O") and (board[2][1] == "O")):
        flag2 = "d"
    #third row check
    elif ((board[0][2] == "X") and (board[1][2] == "X") and (board[2][2] == "X")):
        flag2 = "s"
    elif ((board[0][2] == "O") and (board[1][2] == "O") and (board[2][2] == "O")):
        flag2 = "d"
    return flag2

def axis_check(board):
    flag3 = "r"
    if ((board[0][0] == "X") and (board[1][1] == "X") and (board[2][2] == "X")):
        flag3 = "s"
    elif ((board[0][0] == "O") and (board[1][1] == "O") and (board[2][2] == "O")):
        flag3 = "d"
    if ((board[0][2] == "X") and (board[1][1] == "X") and (board[2][0] == "X")):
        flag3 = "s"
    elif ((board[0][2] == "O") and (board[1][1] == "O") and (board[2][0] == "O")):
        flag3 = "d"
    return flag3

def wining_conditions(board):
    #-----------------------------------------------------------#
    ######################## ROW CHECK ##########################
    #-----------------------------------------------------------#
    flag1 = row_check(board)
    if (flag1 == "s"):
        print(f"\n\n{Fore.GREEN}X won the game{Style.RESET_ALL}")
        f1 = True
    elif (flag1 == "d"):
        print(f"\n\n{Fore.GREEN}O won the game{Style.RESET_ALL}")
        f1 = True
    elif (flag1 == "r"):
        f1 = False
    #-----------------------------------------------------------#
    ####################### COLUMN CHECK ########################
    #-----------------------------------------------------------#
    flag2 = col_check(board)
    if (flag2 == "s"):
        print(f"\n\n{Fore.GREEN}X won the game{Style.RESET_ALL}")
        f2 = True
    elif (flag2 == "d"):
        print(f"\n\n{Fore.GREEN}O won the game{Style.RESET_ALL}")
        f2 = True
    elif (flag2 == "r"):
        f2 = False
    #-----------------------------------------------------------#
    ######################## AXIS CHECK #########################
    #-----------------------------------------------------------#
    flag3 = axis_check(board)
    if (flag3 == "s"):
        print(f"\n\n{Fore.GREEN}X won the game{Style.RESET_ALL}")
        f3 = True
    elif (flag3 == "d"):
        print(f"\n\n{Fore.GREEN}O won the game{Style.RESET_ALL}")
        f3 = True
    elif (flag3 == "r"):
        f3 = False
    return f1, f2, f3


while True:    
    os.system("cls")
    title = "Tick Tack Toe"
    print(Fore.GREEN + (f.renderText(title)) + Style.RESET_ALL)
    print()
    jack = input(f"    Please press {Fore.GREEN}ENTER{Style.RESET_ALL} to continue or {Fore.GREEN}'q'{Style.RESET_ALL} to quit: ")
    if jack == "":
        board = create_board()        
        while True:
            os.system("cls")
            show_board(board)
            board = user_input(board, "X")
            f1, f2, f3 = wining_conditions(board)
            if not((f1 == False) and (f2 == False) and (f3 == False)):
                os.system("cls")
                show_board(board)
                wining_conditions(board)
                jack == input("")
                if jack == "":
                    os.system("cls")
                    show_board(board)
                    wining_conditions(board) 
                    break
            os.system("cls")
            show_board(board)
            board = user_input(board, "O")
            f1, f2, f3 = wining_conditions(board)
            if not((f1 == False) and (f2 == False) and (f3 == False)):
                os.system("cls")
                show_board(board)
                wining_conditions(board)
                jack == input("")
                if jack == "":
                    os.system("cls")
                    show_board(board)
                    wining_conditions(board)
                    break
            
            
    elif jack == "q":
        break
    else:
        continue
