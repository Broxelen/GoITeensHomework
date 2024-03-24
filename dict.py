dict_one = {"apple": 3, "banana": 5, "orange": 2}
dict_two = {"pear": 4, "grape": 6, "kivi": 7}

merged_dict = {}

for key, value in dict_one.items():
    merged_dict[key] = value

for key, value in dict_two.items():
    merged_dict[key] = value

print("Обєднаний словник:", merged_dict)

