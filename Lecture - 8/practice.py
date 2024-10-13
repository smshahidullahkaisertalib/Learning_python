# class Student: 
#     def __init__(self, fullname, marks1, marks2, marks3):
#         self.name = fullname
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3
    
#     def average(self):
#         sum = self.marks1 + self.marks2 + self.marks3
#         avg = sum / 3
#         return avg
    

# s1 = Student("talib", 90, 98, 95)
# print(s1.average())
class Student: 
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

    
    def average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
            avg = sum / len(self.marks)
        return avg
    

s1 = Student("talib", [90, 98, 95, 99, 100])
print(s1.average())

