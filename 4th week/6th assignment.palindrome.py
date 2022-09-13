p = x = int(input('enter any number :'))
c = 0
while True :
    z = x  % 10
    f = x - z
    x = ((f) // (10)) 
    c = (c * 10) + z
    if ((x) // (10)) == 0 :
        c = (c * 10) + x
        break

if c == p :
    print('the given number is PALINDROME')
elif not(c == p) :
    print('the given number is not a PALINDROME')
