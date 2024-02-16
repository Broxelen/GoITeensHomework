first_list = []
second_list = []

while True:
    firstnumber = input("Введіть число (або stop для завершення): ")
    if firstnumber.lower() == "stop":
       break
    else:
        first_list.append(int(firstnumber))
        
       
for num in first_list:
    if num % 2 == 0:
        second_list.append(num)
    
              
           
print(first_list)            
        
print(f"Парні числа{second_list}")
        

    
