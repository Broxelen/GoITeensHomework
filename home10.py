numbers = input("Введіть перву послідовність чисел: ")
numbers2 = input("Введіть другу послідовність чисел: ")

my_set1 = set(numbers)
my_set2 = set(numbers2)

print(my_set1.intersection(my_set2))