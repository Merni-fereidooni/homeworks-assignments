print('a = C -> F')
print('b = F -> C')
print('c = K -> F')
print('d = F -> K')
print('e = C -> K')
print('f = K -> C')



equation = input('please choose on out of the sixth conversions above :')

a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'

temperature = float(input('please enter the temperature in the choosen equation :'))

a1 = (((temperature) * (1.8)) + (32)) 
b2 = (((temperature) - (32)) / (1.8)) 
c3 = ((((temperature) - (273.15)) * (1.8)) + (32)) 
d4 = ((((temperature) - (32)) / (1.8)) - (273.15)) 
e5  = ((temperature) + (273.150)) 
f6  = ((temperature) - (273.15)) 

if equation==a:                   
    print(a1)
elif 'b' :
    print(b2)
elif 'c' :
    print(c3)
elif 'd' :
    print(d4)
elif 'e' :
    print(e5)
elif 'f' :
    print(f6)