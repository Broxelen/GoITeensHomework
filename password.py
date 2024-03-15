import string
import random

long = int(input("Введіть довжину пароля: "))
character = (input("Введіть символи які хочете використовувати в паролі: "))

settings = input("Оберіть опцію яку хочете використовувати.\n a - Пароль з великих літер\n b - пароль з маленьких літер\n c - змішаний пароль(великі, маленькі)\n d - змішаний пароль (великі, маленькі + символи)\n f - зробити пароль з символів що не повторюються")

if settings == "a":
    item = string.ascii_uppercase
elif settings == "b":
    item = string.ascii_lowercase
elif settings == "c":
    item = string.ascii_letters
elif settings == "d":
    item = string.ascii_letters + string.punctuation
elif settings == "f":
    item = ''.join(set(character))
else:
    print("Такої опції не існує")
    
parol = ''.join(random.choice(item) for _ in range(long))

print(f"Ось ваш пароль: {parol}")
    
