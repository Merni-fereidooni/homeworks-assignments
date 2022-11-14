def date(day, month, year):
    date = print(year, "/",month, "/", day, sep="")
    return date

day = int(input("please enter the date of the day: "))
month = int(input("please enter the date of the month: "))
year = int(input("please enter the date of the year: "))

date(day, month, year)