number = float(input('please enter the number :'))

x = (((number) % (100)) // (10))
y = ((x) / (2))
z = ((x) > 3)

if (number < 10) :
    print('please a enter number greater than 9')


elif ((y == 0) and (z)) :
    print('the second digit of the number is an even number and is greater than 3')

elif not((y == 0) and (z)) :
    print('the second digit of the number is neither an even number nor is greater than 3')

elif not(y == 0) and (z) :
    print('the second digit of the number is NOT an even number but is greater than 3 ')

elif (y == 0) and not(z) :
    print('the second digit of the number is an even number but is NOT greater than 3')

else :
    print('invalid number')
    print('please enter a number greater than 0')