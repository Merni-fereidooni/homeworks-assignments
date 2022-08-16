grade_1 = float(input('Enter grade_1 :'))
    
if grade_1 > 10 or grade_1 < 0:                                  
    while grade_1 > 10:
        print('please enter grade_1 lower then 10')
        grade_1 = float(input('Enter grade_1 :'))
        
    while grade_1 < 0:
         print('please enter grade_1 higher then 0')
         grade_1 = float(input('Enter grade_1 :'))

if 0 <= grade_1 <= 10:
 grade_2 = float(input('Enter grade_2 :'))

if grade_2 > 10 or grade_2 < 0:
    while grade_2 > 10:
      print('please enter grade_2 lower then 10')
      grade_2 = float(input('Enter grade_2 :'))
    while grade_2 < 0:
      print('please enter grade_2 higher then 0')
      grade_2 = float(input('Enter grade_2 :'))

if 0 <= grade_2 <= 10:
    grade_3 = float(input('Enter grade_3 :'))

if grade_3 > 10 or grade_3 < 0  :
    while grade_3 > 10:
      print('please enter grade_3 lower then 10')
      grade_3 = float(input('Enter grade_3 :'))
    while grade_3 < 0:
      print('please enter grade_3 higher then 0')
      grade_3 = float(input('Enter grade_3 :'))

if 0 <= grade_3 <= 10:
    testAvg = (grade_1 + grade_2 + grade_3) / 3





if 8 < testAvg <= 10:
    print('your test average is :' ,testAvg)
    print('grade A pass')
elif 5 < testAvg <= 8:
    print('your test average is :' ,testAvg)
    print('pass')
elif 0 < testAvg <= 5:
    print('your test average is :' ,testAvg)
    print('fail')
    
