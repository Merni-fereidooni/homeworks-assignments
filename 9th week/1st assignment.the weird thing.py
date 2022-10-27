def remove(string):
    return string.replace(" ", "")
statement = input('\nplease enter a statement: ')
comma_counter = 0
period_counter = 0
for i in range(len(statement)):
    if statement[i] == ",":
        comma_counter += 1
    if statement[i] == ".":
        period_counter += 1

print("\n\n\n\nyour enterd statement has " , comma_counter , "many commas!")
print("\nyou'r enterd statement has " , period_counter , "many periods!")
print("\nyou'r enterd statement has " , (len(remove(statement)) - (comma_counter) - (period_counter)) , "many characters!")
print("\nyou'r enterd statement has " , (len(statement) - len(remove(statement))) , "many whitespaces!\n\n\n\n")
