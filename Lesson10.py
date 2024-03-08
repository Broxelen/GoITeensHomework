numbers = {1, 2, 3}
numbers.add(4)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.discard(3)
print(numbers)
numbers.discard(2)
print(numbers)
try:
    numbers.remove(2)
except KeyError:
    print("Item not insent")