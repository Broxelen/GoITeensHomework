my_str = input("Enter a string: ")
my_list = []
my_list2 = []

for item in sorted(set(my_str)):
    if my_str.count(item) > 1:
        my_list.append(item)
        
    else:
        my_list2.append(item)
        
while " " in my_list:
    my_list.remove(" ")
    
while " " in my_list2:
    my_list2.remove(" ")
    
        
my_list.sort()
my_list2.sort()
        
print(f"Літери якіі повторюються: {my_list}, Літери які не повторюються: {my_list2}")