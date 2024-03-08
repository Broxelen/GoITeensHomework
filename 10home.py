
input = input("Введіть послідовність: ").split()
numbers = [int(num) for num in input]  

if len(numbers) == len(set(numbers)):
    print("Is unique sequence")
else:
    print("Duplicate list")
