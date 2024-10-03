# greenLightOn = True  

# if(greenLightOn == True):
#     print("go")
# elif(greenLightOn == False):
#     print("stay behind")


marks = int(input("Enter your marks: "))

if(marks >=90):
    print("A+")
elif(marks <= 80 and marks>= 89):
    print("B")
else: 
    print("Not eligible")