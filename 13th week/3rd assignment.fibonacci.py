len = int(input("please enter the length of the sequence: "))


list = [0]
first_statement = 0
second_statement = 1
new_num = 0


for i in range(len - 1):
    new_num = first_statement + second_statement
    second_statement = first_statement
    first_statement = new_num
    list.append(new_num)
print(list)