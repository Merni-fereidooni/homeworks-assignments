import random 
sum_of_roll = 0

while True :
    ans = input("would you like to roll, 'y' for yes, 'n' for no: ")
    if ans == 'y' :
        roll = random.randint(1,6)
        print("roll number","is",":",roll)
        sum_of_roll += roll
    if ans == 'n' :
        print('Game Over!')         
    if roll == 6 :
        print("the sum of all the rolled numbers is",sum_of_roll)
        break