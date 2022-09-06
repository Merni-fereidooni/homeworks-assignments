print('welcom to this weird game that my prof wanted and i went through hell to make it work')
print('so please enjoy u sexy mf ;)')


import random
x = random.randint(0,100)


while True :
    y = print("is your number", x ,",'y' for yes , if no 'lower' or 'greater' : ")
    y = input('')
    if y == 'y' :
        print('Game over')
        break
    if y == 'lower' :
        x -= 1
    if y == 'greater' :
        x += 1
    else :
        print('invalid!')