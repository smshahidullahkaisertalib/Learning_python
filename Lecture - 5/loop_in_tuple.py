tuple = (2,54,68,75,55,89,80)
n = int(input("Enter a number: "))
index = 0
while index <= len(tuple) - 1:
    # print(tuple[index])
    if(n == tuple[index]):
        print(n, "found at index" ,index)
    else:
        print("find more")
    index += 1
        