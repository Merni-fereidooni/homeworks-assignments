statement = list(input("please enter a statement: "))
vowels = ['o' , 'O' , 'u' , 'U' , 'a' , 'A' , 'i' , 'I' , 'e' , 'E']

for i in range(len(statement)):
    for z in range(len(vowels)):
        if statement[i] == vowels[z]:
            statement[i] = "?"
for i in (statement):
    print(i ,end ="")