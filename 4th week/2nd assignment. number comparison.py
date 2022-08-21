print('first user please enter your numbers below.')
no1 = float(input('please enter the first number: '))
no2 = float(input('please enter the second number: '))
no3 = float(input('please enter the third number: '))


print('now its the second users turn .')
no11 = float(input('please enter the first number: '))


if ((abs(no11 - no1) > abs(no11 - no2) > abs(no11 - no3)) or (abs(no11 - no2) > abs(no11 - no1) > abs(no11 - no3))) :
    print('user two number is closer to user one third number')


elif ((abs(no11 - no1) > abs(no11 - no3) > abs(no11 - no2)) or (abs(no11 - no3) > abs(no11 - no1) > abs(no11 - no2))) :
    print('user two number is closer to user one second number')
 

elif ((abs(no11 - no2) > abs(no11 - no3) > abs(no11 - no1)) or (abs(no11 - no3) > abs(no11 - no2) > abs(no11 - no1))) :
    print('user two number is closer to user one first number')
