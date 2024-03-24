stock = {
    "banana": 10,
    "apple": 5,
    "orange": 6,
    "kiwi": 4,
    "watermelon": 3
}

item = input("Оберіть товар який хочете купити: ").lower()
quantiti = int(input("Оберіть кількість: "))

if item in stock and stock[item] >= quantiti:
    print(True)
else:
    print(False)