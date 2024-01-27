x = int(input("X: "))
y = int(input("Y: "))

if x > 0 and y > 0:
    print("Quarter 1")
    
elif x < 0 and y < 0:
    print("Quarter 3")
    
elif x < 0 and y > 0:
    print("Quarter 2")
    
elif x > 0 and y < 0:
    print("Quarter 4")