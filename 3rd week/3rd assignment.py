first_number = float(input('please enter the first number :'))
second_number = float(input('please enter the second number :'))


x = (first_number % second_number) >= (4)
y = (second_number % first_number) >= (4)

z = (first_number / second_number)
o = (second_number / first_number)


if (((z) > 1) or ((z) < 0)) and (x) :
    print('the remainder of the division between the two numbers is higher then 4')
elif (((o) > 1) or ((o) < 0)) and (y) :
    print('the remainder of the division between the two numbers is higher then 4')
else :
    print('the remainder of the division between the two numbers is NOT higher then 4')
