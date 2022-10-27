import random

names = ['shit' , 'fuck' , 'asshole' , 'fuckknuckels' , 'mfucker' , 'dick' , 'dickhead']
x = random.choice(names)
guess_list = []
life_bar = len(x) + 1

for i in range(len(x)):
    guess_list.append('_')

while life_bar > 0 :
    print()
    print(life_bar * '❤ ')

    for i in range(len(x)):
        print(guess_list[i] , end = ' ' )
    print('\n')
    guessed_character = input('guess a character you piece of shit: ')
    counter = 0
    for i in range(len(x)):
        if guessed_character == x[i]:
            guess_list[i] = guessed_character
            counter += 1
    if counter == 0:
        life_bar -= 1
    counter = 0
    for i in guess_list:
        if i == '_':
            counter += 1
    if counter == 0:
        print("you've won")
        break
for i in range(len(guess_list)):
    if guess_list[i] == '_':
        print("\nthe word is: " , x)
        print("\nyou've lost\n")