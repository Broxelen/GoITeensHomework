year = int(input("Введіть рік"))

if year // 4:
    print("Рік є високосним")
    
elif 100 // year // 400:
     print("Рік є високосним")

else:
    print("Рік не є високосним")