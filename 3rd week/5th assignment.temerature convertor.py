print('a. C -> F')
print('b. F -> C')
print('c. K -> F')
print('d. F -> K')
print('e. C -> K')
print('f. K -> C')



equation = input('please choose on out of the sixth conversions above :')
temperature = float(input('please enter the temperature in the choosen equation :'))



a1 = (((temperature) * (1.8)) + (32)) 
b2 = (((temperature) - (32)) / (1.8)) 
c3 = ((((temperature) - (273.15)) * (1.8)) + (32)) 
d4 = ((((temperature) - (32)) / (1.8)) - (273.15)) 
e5  = ((temperature) + (273.150)) 
f6  = ((temperature) - (273.15)) 



if (equation == 'a' ) :                   
    print(a1)
elif (equation == 'b' ) :
    print(b2)
elif (equation == 'c' ) :
    print(c3)
elif (equation == 'e' ) :
    print(d4)
elif (equation == 'f' ) :
    print(e5)
elif (equation == 'g' ) :
    print(f6)
else :
    print('invalid!')
    print('please enter on of the conversions and nothing else')