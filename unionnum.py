my_list1 = [2, 5, 8, 11, 10, 9]
my_list2 = [11, 3, 7, 6, 8, 5]

my_set1 = set(my_list1)
my_set2 = set(my_list2)

intersection = my_set1.intersection(my_set2)

print(sorted(intersection))