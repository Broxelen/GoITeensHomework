import copy

my_friends = [[["Михайло"], ["13"], ["Favorite subject: Physical Education"]], [["Іван"], ["14"], ["Favorite subject: Art"]] ]


friendone = [["Михайло"], ["13"], ["Favorite subject: Physical Education"]]

friendtwo = [["Іван"], ["14"], ["Favorite subject: Art"]]

friendthree = [["Микола"], ["12"], ["Favorite subject: Physical Education"]]

friendfour = [["Михайло"], ["13"], ["Favorite subject: Physical Education"]]

friendfive = [["Артем"], ["13"], ["Favorite subject: Art"]]
for i in friendone:
            my_friends.append(i)
            
for i in friendtwo:
            my_friends.append(i)
            
            
for i in friendthree:
            my_friends.append(i)     


for i in friendfour:
            my_friends.append(i) 
            

for i in friendfive:
            my_friends.append(i)
            print(my_friends)

my_friendcopy = my_friends.copy()
            
my_friends[1] = ["14"]

my_friends[4] = ["15"]

my_friends[7] = ["13"]

my_friends[10] = ["14"]

my_friends[13] = ["14"]



del my_friends[0:6]

del my_friends[3:9]

print(my_friends)

print(my_friendcopy)
            
# мені не надіслали на цей час ніхто список з учнів можливо це моя вина але все що потрібно було я виконав
