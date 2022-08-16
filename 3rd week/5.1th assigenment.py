print('1 = C -> F')
print('2 = F -> C')
print('3 = K -> F')
print('4 = F -> K')
print('5 = C -> K')
print('6 = K -> C')


print('please choose on out of the sixth conversions above press enter until the desired equation is reached then put a period :')

if input(1):
    temperature = float(input('please enter the temperature in the choosen equation :'))
    equation = a1 = (((temperature) * (1.8)) + (32))
    print(a1)
    
elif input(2) :
    temperature = float(input('please enter the temperature in the choosen equation :'))
    equation = b2 = (((temperature) - (32)) / (1.8))
    print(b2)
     
elif input(3) :
    temperature = float(input('please enter the temperature in the choosen equation :'))
    equation = c3 = ((((temperature) - (273.15)) * (1.8)) + (32))
    print(c3)
    
elif input(4) :
    temperature = float(input('please enter the temperature in the choosen equation :'))
    equation = d4 = ((((temperature) - (32)) / (1.8)) - (273.15))
    print(d4)
    
elif input(5) :
    temperature = float(input('please enter the temperature in the choosen equation :'))
    equation = e5 = ((temperature) + (273.150))
    print(e5)
    
elif input(6) :
    temperature = float(input('please enter the temperature in the choosen equation :'))
    equation = f6 = ((temperature) - (273.15))
    print(f6)
    
