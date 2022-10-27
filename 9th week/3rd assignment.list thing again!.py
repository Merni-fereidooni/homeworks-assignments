color_list_user1 = list()
color_list_user2 = list()
while True:
    color = input("please enter a color user1: ")
    color_list_user1.append(color)
    if color == ('-1'):
        break
while True:
    color = input("please enter a color user2: ")
    color_list_user2.append(color)
    if color == ('-1'):
        break

for i in range(len(color_list_user1)):
    if color_list_user2[i] == color_list_user1[i]:
        color_list_user2.remove(color_list_user2[i])
    
print(color_list_user2)