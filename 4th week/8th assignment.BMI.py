x = float(input('please enter your highet in meters :'))
y = float(input('please enter your weight in kg :'))
z = ((y) / ((x) ** (2)))



if 16 <= z < 18.5 :
    print('your BMI is ' ,z)
    print('go eat some shit u need 2 gain weight u skinny bitch')
elif 18.5 <= z < 24 :
    print('your BMI is ' ,z)
    print('u good!')
elif 24 <= z < 30 :
    print('your BMI is ' ,z)
    print('u need 2 lose some weight u look like shit!')
elif 30 <= z <= 45 :
    print('your BMI is ' ,z)
    print('go lose some weight u fat fuck!')
    print('don`t u have a miroir in your room????')
    print('did u really needed a BMI calculator to tell u that u r fat??????')
else :
    print('invalid!')
    print('please check your inputs!')