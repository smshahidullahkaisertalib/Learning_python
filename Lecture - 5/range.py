n = int(input("Enter a number: "))

# seq = range(1, 11)
# for i in seq:
#     print(i*n)

sum = 1
for i in range(1, n+1):
    sum = sum * i
print(sum)