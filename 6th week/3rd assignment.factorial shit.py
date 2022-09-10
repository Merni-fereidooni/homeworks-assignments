y = 1
x = 1
c = int(input('please enter a number: '))
while True :
    y += 1
    x = x * y
    if x == c :
        flag = True
        break
    if x > c :
        flag = False
        break
            
    
if flag == True :
    print(y,'is the root factorial of your number')
elif flag == False :
    print('your number is not the factorail of any number')