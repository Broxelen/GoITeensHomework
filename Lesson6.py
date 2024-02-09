my_list = [4, 5, 4, 1, 1, 0, 5, 2, 2, 4, 4, 2, 4, 5, 3, 2, 1, 4, 1, 0]

unique_list = []
for number in my_list:
    if number not in unique_list:
        unique_list.append(number)
        print(unique_list)