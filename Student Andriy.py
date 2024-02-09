student1 = ["Андрій", "20 років"]

student2 = ["Василь", "19 років"]

student3 = ["Максим", "17 років"]

student4 = ["Андрій", "23 роки"]

my_student = []
for i in student1:
     my_student.append(i)
     
for i in student2:
     my_student.append(i)
     
for i in student3:
     my_student.append(i)
     
for i in student4:
     my_student.append(i)
     print(my_student)

studentandriy = 0
     
studentandriy = sum(True for i in my_student if i == "Андрій")

print(studentandriy)