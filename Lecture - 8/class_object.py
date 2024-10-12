class Student:
    name = ""
    age = int
    Department = ""
    City = ""

student1 = Student()
print(student1)
student1.name = "Talib"
student1.age = 27
student1.Department = "CCE"
student1.City = "Chittagong"

student2 = Student()
print(student2)
student2.name = "Raju"
student2.age = 24
student2.Department = "CCE"
student2.City = "Comilla"

print(student1.name, student1.age, student1.Department, student1.City)
print(student2.name, student2.age, student2.Department, student2.City)
