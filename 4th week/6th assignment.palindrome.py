x = input('enter any number :')
try:
    val = int(x)
    if x == str(x)[:: -1] :
        print('the given number is PALINDROME')
    else :
        print('the given number is not a PALINDROME')
except ValueError :
    print('that ain`t a valid number buddy , Try again!')