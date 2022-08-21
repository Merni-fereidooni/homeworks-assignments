x = int(input('please enter your number :'))

odd_digits = ([int(char) for char in str(x) if int(char) % 2 == 1 ])
even_digits = ([int(char) for char in str(x) if int(char) % 2 == 0 ])

if len(odd_digits) > len(even_digits) :
    print('the number`s odd digits are more then the even digits.') 
elif len(odd_digits) < len(even_digits) :
    print('the number`s even digits are more then the odd digits.')
elif len(odd_digits) == len(even_digits) :
    print('the number`s odd digits are equal to the even digtis') 
