data_list = list()
new_list = list()

for i in range(10) :
    num = int(input('please enter a number: '))
    data_list.append(num)

while data_list:
    minimum = data_list[0]  
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
print(new_list)        
