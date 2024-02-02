print("Enter your number:  ")
numberr = int(input())
number_s = range(numberr)
for number in number_s:
    if number % 2 != 0:
        print(number)