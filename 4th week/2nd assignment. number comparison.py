print('first user please enter your numbers below.')
no1 = float(input('please enter the first number: '))
no2 = float(input('please enter the second number: '))
no3 = float(input('please enter the third number: '))


print('now its the second users turn .')
no11 = float(input('please enter the first number: '))

x = ((no11) - (no1))
y = ((no11) - (no2))
z = ((no11) - (no3))
p = ((abs(no11 - no1) >= abs(no11 - no2) >= abs(no11 - no3)) or (abs(no11 - no2) >= abs(no11 - no1) >= abs(no11 - no3)))
c = ((abs(no11 - no1) >= abs(no11 - no3) >= abs(no11 - no2)) or (abs(no11 - no3) >= abs(no11 - no1) >= abs(no11 - no2)))
f = ((abs(no11 - no2) >= abs(no11 - no3) >= abs(no11 - no1)) or (abs(no11 - no3) >= abs(no11 - no2) >= abs(no11 - no1)))


if (c) and (f) and (p) :
    print('user two number is closer to user one ALL numbers')
elif (p) and (c) :
    print('user two number is closer to user one second and third numbers')
elif (c) and (f) :
    print('user two number is closer to user one first and second numbers')
elif (p) and (f) :
    print('user two number is closer to user one first and third numbers')
elif (p) :
    print('user two number is closer to user one third number')
elif (c) :
    print('user two number is closer to user one second number')
elif (f) :
    print('user two number is closer to user one first number')
