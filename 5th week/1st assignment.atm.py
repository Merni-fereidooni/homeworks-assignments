for i in range (0,3) :
    x = int(float(input('please enter your card`s 4 digit pword: ')))
    while (not((999) < (x) <= (9999))) :
        x = int(float(input('please enter your card`s 4 digit pword: ')))
    if ((x) == (5608)) :
        print('Access Granted')
        break
    elif ((x) == (8065)) :
        print('Alert!')
        print('suspicious Activity!')
        print('reporting to related authoritys')
        print('you are FUCKED!')
        print('BIG Time')
        break
    elif (not(((x) == (5608)) or ((x) == (8065)))) and ((999) < (x) <= (9999)) :
        print('Access Denied')            
if not (((x) == (5608)) or ((x) == (8065))) :
    print('your credit card has declined')
