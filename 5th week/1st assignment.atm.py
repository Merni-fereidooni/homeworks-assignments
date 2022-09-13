for i in range (0,3) :
    pcode = int(input('please enter your card`s 4 digit passcode: '))
    while (not((999) < (pcode) <= (9999))) :
        pcode = int(input('please enter your card`s 4 digit passcode: '))
    if ((pcode) == (5608)) :
        print('Access Granted')
        break
    elif ((pcode) == (8065)) :
        print('Alert!')
        print('suspicious Activity!')
        print('reporting to related authoritys')
        print('you are FUCKED!')
        print('BIG Time')
        break
    elif (not(((pcode) == (5608)) or ((pcode) == (8065)))) and ((999) < (pcode) <= (9999)) :
        print('Access Denied')            
if not (((pcode) == (5608)) or ((pcode) == (8065))) :
    print('your credit card has declined')
