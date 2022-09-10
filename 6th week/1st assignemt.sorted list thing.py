y = list()
for i in range(10) :
    x = int(input('please enter a number: '))
    y.append(x)
for i in range(2,len(y)) :
    if ((y[i - 2] < y[i - 1] > y[i]) or (y[i - 2] < y[i - 1] > y[i])) : 
        flag = False
        break
    if y[i - 2] > y[i - 1] :
        flag = True
        continue 
    if y[i - 2] < y[i - 1] : 
        flag = True
        continue
    else :
        flag = False 
        break

if flag == False :
    print('no')
elif flag == True :
    print('yes') 


