x = float(input('please input the number :'))

y = ((x) % (3))
z = ((((x) // (3)) + (1)) * (3))

if y == 0 :
    print('your number is divisable by 3.')
else :
    print('your number is NOT divisable by 3!')
    print('but the next number divisable by 3 is ' ,z)
