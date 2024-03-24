years_peoples = {
    "Олена": 32,
    "Іван": 45,
    "Марія": 28,
    "Петро": 60,
    "Анна": 50
}

biggest_people = max(years_peoples, key=years_peoples.get)
print(biggest_people)
