number = int(float(input("enter number : ")))

fifth_number = number % 100000 // 10000
second_number = number % 100 // 10

sum = fifth_number + second_number

print("sum of the 2nd and 5th no is :" ,sum)
