list = [1, 2 ,3, 4, 5, 6]
mixedList = ["talib", 27, "chittagong"]

print(list + mixedList)
print(mixedList)

mixedList[0] = "She"
print(mixedList[0:3])

list.pop(2)
list.pop(2)
print(list)

a = ()
b = a + (1, 2)
print(type(b))


