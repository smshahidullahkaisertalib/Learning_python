list = [1, 3, 5, 6,7 ,8]

strings = ['Talib', 'Chittagong', 'IIUC']
print(type(strings))
strings[2] = "Oxford"
print(strings)

strings.append("shoshur bari")
strings.sort(reverse=True)
strings.reverse()

strings.pop(1)
print(strings)

print(list[:]) # returns the whole list

list = [1, 3, 5, 6,7 ,8]
list.insert(2,100)
print(list)
print(len(strings), len(list))