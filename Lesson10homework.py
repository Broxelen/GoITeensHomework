import random

numbers = {random.randint(1, 50) for _ in range(10)}
my_list = list()

while numbers:
    min_elem = min(numbers)
    my_list.append(min_elem)
    numbers.remove(min_elem)
    try:
        max_elem = max(numbers)
    except ValueError:
        break
    my_list.append(max_elem)
    my_list.remove(max_elem)
    
print(my_list)
    
    