import statistics

math = int(input("Enter your marks in math: "))
python = int(input("Enter your marks in python: "))

sum = math + python
print("Math: ", math)
print("python: ", python)
print("total: ", sum)


Marks = [math, python] 
average = statistics.mean(Marks)
print("average is :",average)

# Printing area of a square:

squareSide = float(input("side of square: "))
#squareSide = squareSide * squareSide  #squareSide ** 2 means "squareSide to the power 2" 
print("area is ", squareSide ** 2)   

a = int(input("a :"))
b = int(input("b :"))

print(a>=b)
