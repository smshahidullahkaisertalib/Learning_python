# i = 1
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

# list = [1,2,4,8,16,32,64,128]

# for element in list:
#     print(element)
#     element += 1

tuple = (1,2,4,8,16,32,64,128)

x = int(input("enter a number: "))
index = 0 
for element in tuple:
    if(x == element):
        print(x, "found at index",index)          
        break
    index += 1
else:
    print(element)
print("The End")

