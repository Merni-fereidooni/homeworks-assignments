list = ['ali','atefe','reza','homa','amir','fateme']


for i in range(2) :
    aghazade = input('please enter your name dear aghazade: ')
    print('please enter where do u want to put', aghazade ,'in the list: ')
    index = int(input(''))
    if index == 7 :
        while True :
            print('the list has less then 7 elements!')
            print('please enter a number lower than 7!')
            print('please enter where do u want to put', aghazade ,'in the list: ')
            index = int(input(''))
            if index < 7 :
                break
    list.insert((index - 1) , aghazade)


print(list)