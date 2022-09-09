print('whale cum 2 my not so efficient time convertor')
print('      ⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀\n'
'       ⢀⣠⣶⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣷⣦⣄⣀⣤⣶⣶\n'
'      ⣰⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⠟⠋\n'
'     ⣼⣿⡿⠃⠀⢀⣤⣾⣿⣿⣿⣿⣷⣦⣄⠀⠀⠈⠉⠀⠀⠀\n'
'    ⣸⣿⡿⠁⠀⢠⣿⣿⠟⠉⠀⠈⠉⠛⢿⣿⣷⡄⠀⠀⠀⠀⠀\n'
'   ⢀⣿⣿⡇⠀⠀⣾⣿⡟⠀⠀⢀⣤⣄⠀⠀⠹⣿⣿⡄⠀⠀⠀⠀\n'
'   ⣾⣿⣿⡇⠀⠀⢻⣿⣷⡀⠀⠘⣿⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀\n'
'  ⣼⣿⡿⣿⣿⡄⠀⠈⠻⣿⣿⣷⣿⣿⡿⠃⠀⢀⣿⣿⡇⠀⠀⠀⠀\n'
' ⣰⣿⣿⠁⠹⣿⣿⣦⡀⠀⠈⠉⠛⠋⠉⠀⠀⣠⣾⣿⡟⠀⠀⠀⠀⠀\n'
' ⣿⣿⣧⣤⣤⣬⣿⣿⣿⣶⣦⣤⣤⣤⣴⣶⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀\n'
' ⠙⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀\n')
print("a. hours to secs")
print("b. secs to hours")
x = input('please choose if u want to convert secs to hours or hours to secs : ')

if x == 'b' :
    y = int(input('please enter time in secs : '))
    z = ((y) // (60) // (60))
    c = ((z) * (60) * (60))
    g = (((y) - (c)) // (60))
    p = ((y) - (((z) * (60) * (60)) + ((g) * (60)))) 
    print('the time is',z,'hours and',g,'mins and',p,'secs')
elif x == 'a' :
    y = int(input('please enter hours : '))
    while True :
        c = int(input('please enter mins : '))
        if c > 60 :
            print('invalid!')
            print('mins must be lower than 60')
        if c <= 60 :
            break
    while True :
        g = int(input('please enter secs : '))
        if g > 60 :
            print('invalid!')
            print('secs must be lower than 60')
        if g <= 60 :
            break        
    p = ((c) * (60))
    z = ((y) * (60) * (60))
    n = g + z + p 
    print('the time is in',n,'secs')
else :
    print('invalid!')
    print("please choose one 'a' or 'b' ")