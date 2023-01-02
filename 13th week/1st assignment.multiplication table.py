x = int(input("please enter x number: ")) 
y = int(input("please enter y number: "))


for i in range(1, (y + 1)):
    for j in range(1, (x + 1)):
        print(i * j, end=" ")
    print()