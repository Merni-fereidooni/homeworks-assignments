print('whale cum 2 my not so efficient time convertor')

while True :
    print("a. hours to secs")
    print("b. secs to hours")
    convertion = input('please choose if u want to convert secs to hours or hours to secs : ')
    
    if convertion == 'b' :
        
        total_seconds = int(input('please enter time in secs : '))
        hour = ((total_seconds) // (60) // (60))
        remaining_seconds = ((hour) * (60) * (60))
        minute = (((total_seconds) - (remaining_seconds)) // (60))
        seconds = ((total_seconds) - (((hour) * (60) * (60)) + ((minute) * (60)))) 
        

        print('the time is',hour,'hours and',minute,'mins and',seconds,'secs')
        break
    elif convertion == 'a' :
        
        hour = int(input('please enter hours : '))
        while True :
            
            
            minute = int(input('please enter mins : '))
            if minute > 60 :
                print('invalid!')
                print('mins must be lower than 60')
            if minute <= 60 :
                break
        while True :
            
            
            seconds = int(input('please enter secs : '))
            if seconds > 60 :
                print('invalid!')
                print('secs must be lower than 60')
            if seconds <= 60 :
                break        
        
        
        seconds_in_minutes = ((minute) * (60))
        seconds_in_hours = ((hour) * (60) * (60))
        total_seconds = seconds + seconds_in_hours + seconds_in_minutes 
        

        print('the time is in',total_seconds,'secs')
        break
    else :
        print('invalid!')
        print("please choose one 'a' or 'b' ")