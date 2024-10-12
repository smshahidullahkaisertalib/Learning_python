# file = open("demo.txt")

# data = file.read()
# print(data)
# file.close()

with open("demo.txt", "a") as file:
    data = file.write("\nI am learning Python")
