len = int(input("please enter the length of the diamond: "))
even = (len / 2)
odd = ((len + 1) / 2)
if ((len % 2) == 0):
    for i in range(1, (int(even) + 1)):
            print(((i) * "*"))
            print()
    for i in range(-(int(even)), 0):    
            print((-i) * "*")
            print()
if not((len % 2) == 0):
    for i in range(0, (int(odd) + 1)):
            print((i) * "*")
            print()
    for i in range(-(int(odd) - 1), 0):    
            print((-i) * "*")
            print()
