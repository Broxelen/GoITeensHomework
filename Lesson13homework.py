math_scores = {
    "Yaroslav": [8, 7, 9, 6, 8],
    "Oleh": [10, 9, 8, 10, 10],
    "Andrii": [6, 7, 8, 9, 6]
}

user_name = input("Введіть імя студента: ")

if user_name in math_scores:
    medium_score = sum(math_scores[user_name]) / len(math_scores[user_name])
    print(f"Середній балл студента {user_name}: {medium_score}")
else:
    print("Такий студент не знайдений")
