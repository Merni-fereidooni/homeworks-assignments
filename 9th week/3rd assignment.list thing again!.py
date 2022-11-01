color_list_user1 = list()
color_list_user2 = list()
new_list = list()
counter = 0
while True:
    color = input("please enter a color user1: ")
    if color == ('-1'):
        break
    color_list_user1.append(color)
while True:
    color = input("please enter a color user2: ")
    if color == ('-1'):
        break
    color_list_user2.append(color)
    

for i in range(len(color_list_user2)):
    for z in range(len(color_list_user1)):
        if not(color_list_user2[i] == color_list_user1[z]):
            counter += 1
        elif (color_list_user2[i] == color_list_user1[z]):
            counter = 0
            break
        elif counter == len(color_list_user1): 
            new_list.append(color_list_user2[i])
            counter = 0
            break
    
    
print(new_list)