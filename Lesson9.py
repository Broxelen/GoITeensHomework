palindrom = input("Enter your palindrom: ")
verification = palindrom[::-1]
if palindrom == verification:
    print(f"{verification} is palindrom!")
    
else:
    print("This is not palindrom!!!")