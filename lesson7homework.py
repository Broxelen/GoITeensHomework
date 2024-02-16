my_tasks = []

while True:
    firsttask = input("Введіть завдання (або q для завершення): ")
    if firsttask.lower() == "q":
       break
    else:
       my_tasks.append(firsttask)
       
my_tasks.sort()

for number, item in enumerate(my_tasks, 1):
   print(f"{number}. {item}")



while True:
        twotask = input("Введіть 'd' для видалення завдання, 's' для сортування у зворотньому порядку або 'q' для виходу: ")
        if twotask.lower() == 'q':
            break
        elif twotask.lower() == 'd':
           my_tasks.pop()
        elif twotask.lower() == 's':
            my_tasks.reverse()
            print("Список завдань у зворотньому порядку:")
            print(my_tasks)
            my_tasks.reverse()


