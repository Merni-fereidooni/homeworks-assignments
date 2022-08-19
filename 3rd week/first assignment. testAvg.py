first_grade = float(input('please enter your first grade: '))
second_grade = float(input('please enter your second grade: '))
third_grade = float(input('please enter your third grade: '))


testAvg = (((first_grade) + (second_grade) + (third_grade)) / (3))


if ( 8 < first_grade <= 10 ) and ( 8 < second_grade <= 10 ) and ( 8 < third_grade <= 10 ) :
    print(testAvg)
    print('grade A pass !')

elif ( 5 < first_grade <= 8 ) and ( 5 < second_grade <= 8 ) and ( 5 < third_grade <= 8 ) :
    print(testAvg)
    print('grade B pass !')

elif ( 0 <= first_grade <= 5 ) and ( 0 <= second_grade <= 5 ) and ( 0 <= third_grade <= 5 ) :
    print(testAvg)
    print('fail !')

else :
    print('inaccurate scores !')