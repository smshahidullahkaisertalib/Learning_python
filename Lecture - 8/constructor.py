class Student:
    def __init__(self, name, age, department, city):
        self.name = name
        self.age = age 
        self.department = department
        self.city = city

student1 = Student("Talib", 27, "CCE", "Chittagong")
student2 = Student("Araf", 24, "CCE", "Chittagong")
student3 = Student("Raju", 24, "CCE", "Comilla")

print(student1.name, student1.age, student1.department, student1.city)
print(student2.name, student2.age, student2.department, student2.city)
print(student3.name, student3.age, student3.department, student3.city)

    