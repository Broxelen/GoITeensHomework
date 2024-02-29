my_str = input("Enter string: ")
number_count = 0

for num in my_str:
    if num.isdigit():
        number_count += 1
        
print(number_count)