number = float(input('please enter the number :'))

if number < 10 :
    while number < 10 :
      print('please enter number higher then 9')
      number = float(input('please enter the number :'))


x = (((number) % (100)) // (10))
y = ((x) > (3)) 
z = (x) / 2 


if y or z == 0:
    print('the second digit of your number is higher then 3 and divisible by 2')
else :
    print('the second digit of your number is lower then 3 and not divisible by 2')
