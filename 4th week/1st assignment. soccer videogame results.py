x = 0
z = 0
y = 0
pointstotalA = 0
pointstotalH = 0


while ((x) <= (5)) :
   
    x = ((x) + (1))
   
    gamepoints_A = int(float(input('A please enter your score for this match: ')))
    gamepoints_H = int(float(input('H please enter your score for this match: ')))
   
   
    if gamepoints_A > gamepoints_H :
        print('A won this round!')
        z = ((z) + (3))
    elif gamepoints_A < gamepoints_H :
        print('H won this round!')
        y = ((y) + (3))
    else :
        print('A and H are tied this round!')
   
   
    pointstotalA = pointstotalA + gamepoints_A
    pointstotalH = pointstotalH + gamepoints_H


print('A`s total scores are',pointstotalA) 
print('A total points are',z)

print('H`s total scores are',pointstotalH)
print('H total points are',y)
