print('whale cum to this weird game that my prof wanted and i went through hell to make it work')
print('so please enjoy u sexy mf ;)')


import random

x = (0)
y = (100)
num = random.randint(x,y)

while True :
    num = random.randint(x,y)
    print("is your number", num ,",'y' for yes , if no 'lower' or 'greater' : ")
    ans = input('')

    if ans == 'greater' :
        x = num
    if ans == 'lower' :
        y = num        
    if ans == 'y' :
        print('you`ve WON')
        print('Game over')
        break