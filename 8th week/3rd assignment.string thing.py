first_statement = input("\nplease enter a statement: ")
second_statement = input("\nplease enter the statement with which you wish to split the first statement: ")

new_statement = first_statement.split(second_statement)
print(str(new_statement))
third_statement = input("\nplease enter the statement with which you wish to join the first statement: ")

new_statement = third_statement.join(new_statement)
print(str(new_statement))