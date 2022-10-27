statement = input("please enter a statement: ")
vowels = ['o' , 'O' , 'u' , 'U' , 'a' , 'A' , 'i' , 'I' , 'e' , 'E']

for i in range(len(statement)):
    if (list(statement))[i] == vowels[i]:
        x = (list(statement))[i] = "?"

print(str(x))